import dataclasses
import typing

from .offer_listings_v2 import OfferListingsV2

@dataclasses.dataclass
class OffersV2:
    listings: typing.Optional[OfferListingsV2] = dataclasses.field(metadata={'key': 'Listings'})