import dataclasses
import typing

@dataclasses.dataclass
class SingleIntegerValuedAttribute:
    display_value: typing.Optional[int] = dataclasses.field(metadata={'key': 'DisplayValue'})
    label: typing.Optional[str] = dataclasses.field(metadata={'key': 'Label'})
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})