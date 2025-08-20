import httpx

from ..transports import ResponseDict, Transport, AsyncTransport

class UseHttpxTransport(Transport, AsyncTransport):
    def __init__(self, client: httpx.Client | None = None, async_client: httpx.AsyncClient | None = None):
        self.client = client or httpx.Client()
        self.async_client = async_client or httpx.AsyncClient()

    def send(self, 
        method: str,
        url: str,
        headers: dict[str, str] = None,
        body: bytes = None
    ):
        res = self.client.request(method, url, headers=headers, content=body)
        return ResponseDict(**{
            "status_code": res.status_code,
            "headers": dict(res.headers),
            "body": res.text,
        })

    async def send(self, 
        method: str,
        url: str,
        headers: dict[str, str] = None,
        body: bytes = None
    ):
        res = await self.async_client.request(method, url, headers=headers, content=body)
        return ResponseDict(**{
            "status_code": res.status_code,
            "headers": dict(res.headers),
            "body": res.text,
        })