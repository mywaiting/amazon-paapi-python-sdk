import dataclasses
import typing

from .rental_offer_listing import RentalOfferListing

@dataclasses.dataclass
class RentalOffers:
    listings: typing.Optional[list[RentalOfferListing]] = dataclasses.field(metadata={'key': 'Listings'})