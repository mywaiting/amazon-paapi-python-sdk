import tornado.httpclient

from ..transports import ResponseDict, AsyncTransport

class UseTornadoTransport(AsyncTransport):
    def __init__(self, client: tornado.httpclient.AsyncHTTPClient = None):
        self.client = client or tornado.httpclient.AsyncHTTPClient()

    async def send(self, 
        method: str,
        url: str,
        headers: dict[str, str] = None,
        body: bytes = None
    ):
        req = tornado.httpclient.HTTPRequest(url, method=method, headers=headers, body=body)
        res = await self.client.fetch(req)
        return ResponseDict(**{
            "status_code": res.code,
            "headers": dict(res.headers),
            "body": res.body.decode("utf-8"),
        })