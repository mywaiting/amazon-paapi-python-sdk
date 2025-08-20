import dataclasses
import typing

from .browse_node_info import BrowseNodeInfo
from .customer_reviews import CustomerReviews
from .images import Images
from .item_info import ItemInfo
from .offers import Offers
from .offers_v2 import OffersV2
from .rental_offers import RentalOffers
from .variation_attribute import VariationAttribute

@dataclasses.dataclass
class Item:
    asin: typing.Optional[str] = dataclasses.field(metadata={'key': 'ASIN'})
    browse_node_info: typing.Optional[BrowseNodeInfo] = dataclasses.field(metadata={'key': 'BrowseNodeInfo'})
    customer_reviews: typing.Optional[CustomerReviews] = dataclasses.field(metadata={'key': 'CustomerReviews'})
    detail_page_url: typing.Optional[str] = dataclasses.field(metadata={'key': 'DetailPageURL'})
    images: typing.Optional[Images] = dataclasses.field(metadata={'key': 'Images'})
    item_info: typing.Optional[ItemInfo] = dataclasses.field(metadata={'key': 'ItemInfo'})
    offers: typing.Optional[Offers] = dataclasses.field(metadata={'key': 'Offers'})
    offers_v2: typing.Optional[OffersV2] = dataclasses.field(metadata={'key': 'OffersV2'})
    parent_asin: typing.Optional[str] = dataclasses.field(metadata={'key': 'ParentASIN'})
    rental_offers: typing.Optional[RentalOffers] = dataclasses.field(metadata={'key': 'RentalOffers'})
    score: typing.Optional[float] = dataclasses.field(metadata={'key': 'Score'})
    variation_attributes: typing.Optional[list[VariationAttribute]] = dataclasses.field(metadata={'key': 'VariationAttributes'})