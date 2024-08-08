from __future__ import annotations

from blib import AsyncTransport, FileSize, deprecated
from cgi import parse_header
from typing import TYPE_CHECKING

from .document import Document
from .enums import StatusCode
from .error import BodyTooLargeError, GeminiError
from .misc import Url

try:
	from typing import Self

except ImportError:
	from typing_extensions import Self

if TYPE_CHECKING:
	from .server import AsyncServer


class Message:
	"Represents a protocol message"

	transport: AsyncTransport
	"The transport associated with the message"

	url: Url
	"URL of the resource after redirects if any"

	origin_url: Url
	"URL of the initial request"

	body: bytes
	"Main part of the message"


	def __init__(self) -> None:
		self._read_body: bool = False


	async def __aenter__(self) -> Self:
		return self


	async def __aexit__(self, *_: None) -> None:
		try:
			await self.transport.close()

		except Exception:
			pass


	@property
	def local(self) -> str:
		"Address of the local socket"

		return self.transport.local_address


	@property
	def remote(self) -> str:
		"Address of the remote socket"

		return self.transport.remote_address


	def build(self) -> bytes:
		"Convert the message into a bytes object that can be sent via a socket"

		raise NotImplementedError("Message.compile")


	async def data(self, limit: FileSize | int = FileSize(256, "MiB")) -> bytes:
		"""
			Read the body of the response. The data gets stored in :attr:`Message.body`.

			:param limit: Max body size to be accepted
			:raises BodyTooLargeError: When the length of the body is higher than the limit
		"""

		if not self._read_body:
			while len(self.body) < limit:
				chunk = await self.transport.read(256)
				self.body += chunk

				if len(chunk) < 256:
					return self.body

			raise BodyTooLargeError(len(self.body), limit)

		return self.body


	@deprecated("data", "0.1.4", "0.2.0")
	async def read_body(self, limit: FileSize | int = FileSize(256, "MiB")) -> bytes:
		"""
			Read the body of the response

			.. note:: Deprecated since 0.1.4. Use :meth:`Message.raw` instead.

			:param limit: Max body size to be accepted
			:raises BodyTooLargeError: When the length of the body is higher than the limit
		"""

		return await self.data(limit)


	async def text(self) -> str:
		"Read the body of the response as a string"

		body = await self.data()
		return body.decode("utf-8")


	async def document(self) -> Document:
		"Read the body and attempt to parse it as a gemtext document"

		return Document.loads(await self.text())


class Request(Message):
	"Represents a client request message"

	server: AsyncServer


	def __init__(self, url: Url | str):
		"""
			Create a new request object

			:param url: URL to send the request to
		"""

		Message.__init__(self)

		self.url: Url = Url.parse(url)


	@classmethod
	async def from_transport(cls: type[Self],
							server: AsyncServer,
							transport: AsyncTransport) -> Self:
		"""
			Parse an incoming client request

			:param server: Server the request will be related to
			:param transport: The transport of the server the request is being sent to
		"""

		try:
			url = (await transport.readline(1024)).decode("utf-8")

		except ValueError as error:
			if "separator is found" in str(error).lower():
				raise GeminiError(59, "Header too long")

		if url.startswith("/"):
			url = f"gemini://{transport.local_address}:{transport.local_port}{url}"

		request = cls(url)
		request.server = server
		request.transport = transport
		return request


	@property
	def path(self) -> str:
		"Path portion of the url"

		return self.url.path


	@property
	def query(self) -> tuple[str, ...]:
		"Query portion of the url"

		return self.url.query


	@property
	def anchor(self) -> str | None:
		"Anchor portion of the url"

		return self.url.anchor


	@property
	def remote(self) -> str:
		"IP address of the remote socket"

		return self.transport.remote_address


	def build(self) -> bytes:
		return f"{self.url}\r\n".encode("utf-8")


class Response(Message):
	"Represents a server response message"

	_mimetype: str
	_mimeopt: dict[str, str]


	def __init__(self,
				status: StatusCode | int,
				body: str | bytes = b"",
				meta: str = ""):
		"""
			Create a new response object

			:param status: Status code of the response
			:param body: Data to be sent
			:param meta: Metadata to be sent
		"""

		Message.__init__(self)

		self.status: StatusCode = StatusCode.parse(status)
		"Status code of the response"

		self.meta: str = meta
		"Metadata (usually mimetype of the data) to be sent with the response"

		self.body: bytes = body if isinstance(body, bytes) else bytes(body, encoding = "utf-8")
		"Data to be sent with the response"


	@classmethod
	async def from_transport(cls: type[Self], transport: AsyncTransport) -> Self:
		"""
			Parse an incoming client request

			:param transport: The transport of the client the response is being sent to
		"""

		try:
			header = (await transport.readline(1024)).decode("utf-8")

		except ValueError as error:
			if "separator is found" in str(error).lower():
				raise GeminiError(59, "Header too long")

		try:
			status, meta = header.strip().split(" ", 1)

		except ValueError:
			status, meta = header, ""

		response = cls(int(status.strip()), meta = meta.strip())
		response.transport = transport
		return response


	@classmethod
	def new_text(cls: type[Self],
				status: StatusCode | int,
				body: str,
				meta: str = "text/plain") -> Self:
		"""
			Create a new response with a text body

			:param status: Status code of the response
			:param body: Text to be sent as the body
			:param meta: Metadata of the response
		"""

		return cls(status, body.encode("utf-8"), meta)


	@property
	def charset(self) -> str:
		return self.mimeopts.get("charset", "utf-8")


	@property
	def mimeopts(self) -> dict[str, str]:
		if not hasattr(self, "_mimeopt"):
			mimetype, options = parse_header(self.meta)
			self._mimetype = mimetype
			self._mimeopt = options

		return self._mimeopt


	@property
	def mimetype(self) -> str:
		if not hasattr(self, "_mimetype"):
			mimetype, options = parse_header(self.meta)
			self._mimetype = mimetype
			self._mimeopt = options

		return self._mimetype


	async def document(self) -> Document:
		"Read the body and attempt to parse it as a gemtext document"

		if not self.mimetype == "text/gemini":
			raise TypeError("Message is not a gemtext document")

		return Document.loads(await self.text())


	async def text(self) -> str:
		"Read the body of the response as a string"

		body = await self.data()
		return body.decode(self.charset)


	def build(self) -> bytes:
		if not self.meta:
			header = str(self.status.value)

		else:
			header = f"{self.status.value} {self.meta}"

		return (header + "\r\n").encode("utf-8") + self.body
