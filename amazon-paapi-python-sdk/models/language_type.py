import dataclasses
import typing

@dataclasses.dataclass
class LanguageType:
    display_value: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayValue'})
    type: typing.Optional[str] = dataclasses.field(metadata={'key': 'Type'})