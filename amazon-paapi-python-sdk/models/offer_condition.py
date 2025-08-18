import dataclasses
import typing

from .offer_sub_condition import OfferSubCondition
from .offer_condition_note import OfferConditionNote

@dataclasses.dataclass
class OfferCondition:
    display_value: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayValue'})
    label: typing.Optional[str] = dataclasses.field(metadata={'key': 'Label'})
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})
    value: typing.Optional[str] = dataclasses.field(metadata={'key': 'Value'})
    sub_condition: typing.Optional[OfferSubCondition] = dataclasses.field(metadata={'key': 'SubCondition'})
    condition_note: typing.Optional[OfferConditionNote] = dataclasses.field(metadata={'key': 'ConditionNote'})