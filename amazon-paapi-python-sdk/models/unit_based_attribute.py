import dataclasses
import typing

@dataclasses.dataclass
class UnitBasedAttribute:
    display_value: typing.Optional[float] = dataclasses.field(metadata={'key': 'DisplayValue'})
    label: typing.Optional[str] = dataclasses.field(metadata={'key': 'Label'})
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})
    unit: typing.Optional[str] = dataclasses.field(metadata={'key': 'Unit'})