import dataclasses
import typing

@dataclasses.dataclass
class SingleStringValuedAttribute:
    display_value: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayValue'})
    label: typing.Optional[str] = dataclasses.field(metadata={'key': 'Label'})
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})