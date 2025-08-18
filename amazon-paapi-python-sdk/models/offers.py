import dataclasses
import typing

from .offer_listing import OfferListing
from .offer_summary import OfferSummary

@dataclasses.dataclass
class Offers:
    listings: typing.Optional[list[OfferListing]] = dataclasses.field(metadata={'key': 'Listings'})
    summaries: typing.Optional[list[OfferSummary]] = dataclasses.field(metadata={'key': 'Summaries'})