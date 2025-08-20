import dataclasses
import typing

@dataclasses.dataclass
class Rating:
    value: typing.Optional[float] = dataclasses.field(metadata={'key': 'Value'})