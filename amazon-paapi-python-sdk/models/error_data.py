import dataclasses
import typing

@dataclasses.dataclass
class ErrorData:
    code: typing.Optional[str] = dataclasses.field(metadata={'key': 'Code'})
    message: typing.Optional[str] = dataclasses.field(metadata={'key': 'Message'})