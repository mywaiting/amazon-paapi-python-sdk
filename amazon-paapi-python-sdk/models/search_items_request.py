import dataclasses
import typing

from .availability import Availability
from .condition import Condition
from .delivery_flag import DeliveryFlag
from .max_price import MaxPrice
from .merchant import Merchant
from .min_price import MinPrice
from .min_reviews_rating import MinReviewsRating
from .min_saving_percent import MinSavingPercent
from .offer_count import OfferCount
from .partner_type import PartnerType
from .properties import Properties
from .search_items_resource import SearchItemsResource
from .sort_by import SortBy

@dataclasses.dataclass
class SearchItemsRequest:
    actor: typing.Optional[str] = dataclasses.field(metadata={'key': 'Actor'})
    artist: typing.Optional[str] = dataclasses.field(metadata={'key': 'Artist'})
    author: typing.Optional[str] = dataclasses.field(metadata={'key': 'Author'})
    availability: typing.Optional[Availability] = dataclasses.field(metadata={'key': 'Availability'})
    brand: typing.Optional[str] = dataclasses.field(metadata={'key': 'Brand'})
    browse_node_id: typing.Optional[str] = dataclasses.field(metadata={'key': 'BrowseNodeId'})
    condition: typing.Optional[Condition] = dataclasses.field(metadata={'key': 'Condition'})
    currency_of_preference: typing.Optional[str] = dataclasses.field(metadata={'key': 'CurrencyOfPreference'})
    delivery_flags: typing.Optional[list[DeliveryFlag]] = dataclasses.field(metadata={'key': 'DeliveryFlags'})
    item_count: typing.Optional[int] = dataclasses.field(metadata={'key': 'ItemCount'})
    item_page: typing.Optional[int] = dataclasses.field(metadata={'key': 'ItemPage'})
    keywords: typing.Optional[str] = dataclasses.field(metadata={'key': 'Keywords'})
    languages_of_preference: typing.Optional[list[str]] = dataclasses.field(metadata={'key': 'LanguagesOfPreference'})
    marketplace: typing.Optional[str] = dataclasses.field(metadata={'key': 'Marketplace'})
    max_price: typing.Optional[MaxPrice] = dataclasses.field(metadata={'key': 'MaxPrice'})
    merchant: typing.Optional[Merchant] = dataclasses.field(metadata={'key': 'Merchant'})
    min_price: typing.Optional[MinPrice] = dataclasses.field(metadata={'key': 'MinPrice'})
    min_reviews_rating: typing.Optional[MinReviewsRating] = dataclasses.field(metadata={'key': 'MinReviewsRating'})
    min_saving_percent: typing.Optional[MinSavingPercent] = dataclasses.field(metadata={'key': 'MinSavingPercent'})
    offer_count: typing.Optional[OfferCount] = dataclasses.field(metadata={'key': 'OfferCount'})
    partner_tag: typing.Optional[str] = dataclasses.field(metadata={'key': 'PartnerTag'})
    partner_type: typing.Optional[PartnerType] = dataclasses.field(metadata={'key': 'PartnerType'})
    properties: typing.Optional[Properties] = dataclasses.field(metadata={'key': 'Properties'})
    resources: typing.Optional[list[SearchItemsResource]] = dataclasses.field(metadata={'key': 'Resources'})
    search_index: typing.Optional[str] = dataclasses.field(metadata={'key': 'SearchIndex'})
    sort_by: typing.Optional[SortBy] = dataclasses.field(metadata={'key': 'SortBy'})
    title: typing.Optional[str] = dataclasses.field(metadata={'key': 'Title'})