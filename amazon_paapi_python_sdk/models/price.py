import dataclasses
import typing

from .offer_price import OfferPrice

@dataclasses.dataclass
class Price:
    highest_price: typing.Optional[OfferPrice] = dataclasses.field(metadata={'key': 'HighestPrice'})
    lowest_price: typing.Optional[OfferPrice] = dataclasses.field(metadata={'key': 'LowestPrice'})