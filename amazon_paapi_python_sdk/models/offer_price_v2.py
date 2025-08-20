import dataclasses
import typing

from .money import Money
from .offer_savings_v2 import OfferSavingsV2
from .offer_saving_basis import OfferSavingBasis

@dataclasses.dataclass
class OfferPriceV2:
    money: typing.Optional[Money] = dataclasses.field(metadata={'key': 'Money'})
    price_per_unit: typing.Optional[Money] = dataclasses.field(metadata={'key': 'PricePerUnit'})
    savings: typing.Optional[OfferSavingsV2] = dataclasses.field(metadata={'key': 'Savings'})
    saving_basis: typing.Optional[OfferSavingBasis] = dataclasses.field(metadata={'key': 'SavingBasis'})