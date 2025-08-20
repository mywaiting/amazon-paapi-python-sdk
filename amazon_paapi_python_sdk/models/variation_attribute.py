import dataclasses
import typing

@dataclasses.dataclass
class VariationAttribute:
    name: typing.Optional[str] = dataclasses.field(metadata={'key': 'Name'})
    value: typing.Optional[str] = dataclasses.field(metadata={'key': 'Value'})