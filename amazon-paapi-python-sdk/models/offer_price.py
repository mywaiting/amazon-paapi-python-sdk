import dataclasses
import typing

from .price_type import PriceType
from .offer_savings import OfferSavings

@dataclasses.dataclass
class OfferPrice:
    amount: typing.Optional[float] = dataclasses.field(metadata={'key': 'Amount'})
    currency: typing.Optional[str] = dataclasses.field(metadata={'key': 'Currency'})
    display_amount: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayAmount'})
    price_per_unit: typing.Optional[float] = dataclasses.field(metadata={'key': 'PricePerUnit'})
    price_type: typing.Optional[PriceType] = dataclasses.field(metadata={'key': 'PriceType'})
    price_type_label: typing.Optional[str] = dataclasses.field(metadata={'key': 'PriceTypeLabel'})
    savings: typing.Optional[OfferSavings] = dataclasses.field(metadata={'key': 'Savings'})