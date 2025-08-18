import typing

from .errors import (
    AccessDenied,
    AccessDeniedAwsUsers,
    InvalidAssociate,
    IncompleteSignature,
    InvalidPartnerTag,
    InvalidSignature,
    TooManyRequests,
    RequestExpired,
    InvalidParameterValue,
    MissingParameter,
    UnknownOperation,
    UnrecognizedClient,
    InvalidArgument
)

from .models import from_dict, to_dict
from .models.hosts import Hosts
from .models.regions import Regions
from .models.partner_type import PartnerType
from .models.item_id_type import ItemIdType
from .models.condition import Condition
from .models.merchant import Merchant
from .models.offer_count import OfferCount
from .models.availability import Availability
from .models.delivery_flag import DeliveryFlag
from .models.properties import Properties
from .models.search_index import SearchIndex
from .models.sort_by import SortBy
from .models.get_browse_nodes_resource import GetBrowseNodesResource
from .models.get_browse_nodes_request import GetBrowseNodesRequest
from .models.get_browse_nodes_response import GetBrowseNodesResponse
from .models.get_items_resource import GetItemsResource
from .models.get_items_request import GetItemsRequest
from .models.get_items_response import GetItemsResponse
from .models.get_variations_resource import GetVariationsResource
from .models.get_variations_request import GetVariationsRequest
from .models.get_variations_response import GetVariationsResponse
from .models.search_items_resource import SearchItemsResource
from .models.search_items_request import SearchItemsRequest
from .models.search_items_response import SearchItemsResponse

from .utils import get_asin


class PaapiClient:
    def __init__(self,
        access_key: str,
        secret_key: str,
        partner_tag: str,
        host: Hosts = Hosts.UNITED_STATES,
        region: Regions = Regions.UNITED_STATES,
    ):
        self.access_key = access_key
        self.secret_key = secret_key
        self.partner_tag = partner_tag
        self.host = host
        self.region = region

    def get_browse_nodes(self, 
        browse_node_ids: typing.List[str],
        languages_of_preference: typing.List[str] = None,
        marketplace: str = None,
        partner_tag: str = None,
        partner_type: PartnerType = PartnerType.ASSOCIATES,
        resources: typing.List[GetBrowseNodesResource] = list(
            GetBrowseNodesResource.BROWSENODES_ANCESTOR,
            GetBrowseNodesResource.BROWSENODES_CHILDREN
        )
    ):
        """returns the specified browse node’s information like name, children and ancestors

        docs: https://webservices.amazon.com/paapi5/documentation/getbrowsenodes.html
        """
        if not isinstance(browse_node_ids, list):
            raise InvalidArgument("Invalid browse_item_ids argument, it should be a List of strings")
        
        get_browse_nodes_request = from_dict(GetBrowseNodesRequest, dict(
            browse_node_ids=browse_node_ids,
            languages_of_preference=languages_of_preference,
            marketplace=marketplace,
            partner_tag=partner_tag,
            partner_type=partner_type,
            resources=resources
        ))
        
    def get_items(self,
        item_ids: typing.Union[str, typing.List[str]],
        item_id_type: ItemIdType = ItemIdType.ASIN,
        condition: Condition = None,
        merchant: Merchant = None,
        offer_count: OfferCount = 1,
        currency_of_preference: str = None,
        languages_of_preference: typing.List[str] = None,
        marketplace: str = None,
        partner_tag: str = None,
        partner_type: PartnerType = PartnerType.ASSOCIATES,
        resources: typing.List[GetItemsResource] = list(
            GetItemsResource.ITEMINFO_TITLE
        )
    ):
        """some or all of the item attributes

        docs: https://webservices.amazon.com/paapi5/documentation/get-items.html
        """
        if not isinstance(item_ids, str) and not isinstance(item_ids, list):
            raise InvalidArgument("Invalid items argument, it should be a string or List of strings")
        
        if isinstance(item_ids, str):
            item_ids = [ get_asin(x.strip()) for x in item_ids.split(",") ]
        else:
            item_ids = [ get_asin(x.strip()) for x in item_ids ]

        get_item_request = from_dict(GetItemsRequest, dict(
            item_ids=item_ids,
            item_id_type=item_id_type,
            condition=condition,
            merchant=merchant,
            offer_count=offer_count,
            currency_of_preference=currency_of_preference,
            languages_of_preference=languages_of_preference,
            marketplace=marketplace,
            partner_tag=partner_tag,
            partner_type=partner_type,
            resources=resources
        ))

    def get_variations(self,
        asin: str,
        variation_count: int = 10,
        variation_page: int = 1,
        condition: Condition = None,
        merchant: Merchant = None,
        offer_count: OfferCount = 1,
        currency_of_preference: str = None,
        languages_of_preference: typing.List[str] = None,
        marketplace: str = None,
        partner_tag: str = None,
        partner_type: PartnerType = PartnerType.ASSOCIATES,
        resources: typing.List[GetVariationsResource] = list(
            GetVariationsResource.ITEMINFO_TITLE
        )
    ):
        """returns a set of items that are the same product, but differ according to a consistent theme

        docs: https://webservices.amazon.com/paapi5/documentation/get-variations.html
        """
        variation_args = [variation_count, variation_page]
        variation_args = [arg for arg in variation_args if arg]

        if not all(isinstance(arg, int) for arg in variation_args):
            raise InvalidArgument("variation_count and variation_page should be integers.")

        if not all(1 <= arg <= 10 for arg in variation_args):
            raise InvalidArgument("variation_count and variation_page should be integers between 1 and 10.")

        get_variations_request = from_dict(GetVariationsRequest, dict(
            asin=asin,
            variation_count=variation_count,
            variation_page=variation_page,
            condition=condition,
            merchant=merchant,
            offer_count=offer_count,
            currency_of_preference=currency_of_preference,
            languages_of_preference=languages_of_preference,
            marketplace=marketplace,
            partner_tag=partner_tag,
            partner_type=partner_type,
            resources=resources
        ))

    def search_items(self,
        keywords: str = None,
        actor: str = None,
        artist: str = None,
        author: str = None,
        brand: str = None,
        title: str = None,
        browse_node_id: str = None,
        item_count: int = None,
        item_page: int = None,
        availability: Availability = Availability.AVAILABLE,
        condition: Condition = Condition.ANY,
        delivery_flags: typing.List[DeliveryFlag] = None,
        max_price: int = None,
        min_price: int = None,
        min_saving_percent: int = None,
        min_reviews_rating: int = None,
        offer_count: OfferCount = 1,
        search_index: SearchIndex = SearchIndex.ALL,
        sort_by: SortBy = None,
        merchant: Merchant = None,
        currency_of_preference: str = None,
        languages_of_preference: typing.List[str] = None,
        marketplace: str = None,
        partner_tag: str = None,
        partner_type: PartnerType = PartnerType.ASSOCIATES,
        properties: Properties = None,
        resources: typing.List[SearchItemsResource] = list(
            SearchItemsResource.ITEMINFO_TITLE
        )
    ):
        """searches for items on Amazon based on a search query

        docs: https://webservices.amazon.com/paapi5/documentation/search-items.html
        """
        mandatory_args = [
            keywords, actor, artist, author, brand, title, browse_node_id, search_index
        ]
        if all(arg is None for arg in mandatory_args):
            raise InvalidArgument(
                "At least one of the following args should be provided: keywords, actor,"
                " artist, author, brand, title, browse_node_id or search_index."
            )
        
        pagination_args = [item_count, item_page]
        pagination_args = [arg for arg in pagination_args if arg]

        if not all(isinstance(arg, int) for arg in pagination_args):
            raise InvalidArgument("item_count and item_page should be integers.")

        if not all(1 <= arg <= 10 for arg in pagination_args):
            raise InvalidArgument("item_count and item_page should be integers between 1 and 10.")

        search_items_request = from_dict(SearchItemsRequest, dict(
            keywords=keywords,
            actor=actor,
            artist=artist,
            author=author,
            brand=brand,
            title=title,
            browse_node_id=browse_node_id,
            item_count=item_count,
            item_page=item_page,
            availability=availability,
            condition=condition,
            delivery_flags=delivery_flags,
            max_price=max_price,
            min_price=min_price,
            min_saving_percent=min_saving_percent,
            min_reviews_rating=min_reviews_rating,
            offer_count=offer_count,
            search_index=search_index,
            sort_by=sort_by,
            merchant=merchant,
            currency_of_preference=currency_of_preference,
            languages_of_preference=languages_of_preference,
            marketplace=marketplace,
            partner_tag=partner_tag,
            partner_type=partner_type,
            properties=properties,
            resources=resources
        ))

