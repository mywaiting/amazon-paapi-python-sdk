import requests

from ..transports import ResponseDict, Transport

class UseRequestsTransport(Transport):
    def __init__(self, session: requests.Session = None):
        self.session = session or requests.Session()

    def send(self, 
        method: str,
        url: str,
        headers: dict[str, str] = None,
        body: bytes = None
    ):
        res = self.session.request(method, url, headers=headers, data=body)
        return ResponseDict(**{
            "status_code": res.status_code,
            "headers": dict(res.headers),
            "body": res.text,
        })