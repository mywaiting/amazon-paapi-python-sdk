import dataclasses
import typing

@dataclasses.dataclass
class SingleBooleanValuedAttribute:
    display_value: typing.Optional[bool] = dataclasses.field(metadata={'key': 'DisplayValue'})
    label: typing.Optional[str] = dataclasses.field(metadata={'key': 'Label'})
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})