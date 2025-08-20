import dataclasses
import typing

@dataclasses.dataclass
class OfferConditionNote:
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})
    value: typing.Optional[str] = dataclasses.field(metadata={'key': 'Value'})