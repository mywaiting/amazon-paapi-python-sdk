import dataclasses
import typing

@dataclasses.dataclass
class RequestDict:
    method: str
    url: str
    headers: dict[str, str]
    body: str

@dataclasses.dataclass
class ResponseDict:
    status_code: int
    headers: dict[str, str]
    body: str

class Transport(typing.Protocol):
    def send(self, 
        method: str, 
        url: str, 
        headers: dict[str, str] = None, 
        body: bytes = None
    ) -> ResponseDict:
        ...

class AsyncTransport(typing.Protocol):
    async def send(self, 
        method: str, 
        url: str, 
        headers: dict[str, str] = None, 
        body: bytes = None
    ) -> ResponseDict:
        ...