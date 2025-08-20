import dataclasses
import typing

from .language_type import LanguageType

@dataclasses.dataclass
class Languages:
    display_values: typing.Optional[list[LanguageType]] = dataclasses.field(metadata={'key': 'DisplayValues'})
    label: typing.Optional[str] = dataclasses.field(metadata={'key': 'Label'})
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})