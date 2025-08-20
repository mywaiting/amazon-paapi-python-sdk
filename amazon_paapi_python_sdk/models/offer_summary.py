import dataclasses
import typing

from .offer_condition import OfferCondition
from .offer_price import OfferPrice

@dataclasses.dataclass
class OfferSummary:
    condition: typing.Optional[OfferCondition] = dataclasses.field(metadata={'key': 'Condition'})
    highest_price: typing.Optional[OfferPrice] = dataclasses.field(metadata={'key': 'HighestPrice'})
    lowest_price: typing.Optional[OfferPrice] = dataclasses.field(metadata={'key': 'LowestPrice'})
    offer_count: typing.Optional[int] = dataclasses.field(metadata={'key': 'OfferCount'})