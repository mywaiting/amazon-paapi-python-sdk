import dataclasses
import typing

@dataclasses.dataclass
class VariationDimension:
    display_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayName'})
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})
    name: typing.Optional[str] = dataclasses.field(metadata={'key': 'Name'})
    values: typing.Optional[list[str]] = dataclasses.field(metadata={'key': 'Values'})