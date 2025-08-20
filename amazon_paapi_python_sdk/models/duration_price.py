import dataclasses
import typing

from .offer_price import OfferPrice
from .unit_based_attribute import UnitBasedAttribute

@dataclasses.dataclass
class DurationPrice:
    price: typing.Optional[OfferPrice] = dataclasses.field(metadata={'key': 'Price'})
    duration: typing.Optional[UnitBasedAttribute] = dataclasses.field(metadata={'key': 'Duration'})