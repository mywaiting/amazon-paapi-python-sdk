import dataclasses
import typing

@dataclasses.dataclass
class MultiValuedAttribute:
    display_values: typing.Optional[list[str]] = dataclasses.field(metadata={'key': 'DisplayValues'})
    label: typing.Optional[str] = dataclasses.field(metadata={'key': 'Label'})
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})