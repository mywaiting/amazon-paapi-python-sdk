"""Amazon Product Advertising API 5.0 rewrited for Python."""

from .__version__ import (
    version,
    version_tuple,
    __version__,
    __version_tuple__
)
from .api import (
    BasePaapiClient,
    PaapiClient,
    AsyncPaapiClient
)
from .auth.awsv4 import AWSV4Auth
from .errors import (
    PaapiError,
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
    AsinNotFound,
    InvalidArgument,
    RequestFailed
)
from .models import from_dict, to_dict
from .models.availability import Availability
from .models.big_decimal import BigDecimal
from .models.browse_node import BrowseNode
from .models.browse_node_ancestor import BrowseNodeAncestor
from .models.browse_node_child import BrowseNodeChild
from .models.browse_node_info import BrowseNodeInfo
from .models.browse_nodes_result import BrowseNodesResult
from .models.by_line_info import ByLineInfo
from .models.classifications import Classifications
from .models.client_exception import ClientException
from .models.condition import Condition
from .models.content_info import ContentInfo
from .models.content_rating import ContentRating
from .models.contributor import Contributor
from .models.country_codes import CountryCodes
from .models.customer_reviews import CustomerReviews
from .models.deal_details import DealDetails
from .models.delivery_flag import DeliveryFlag
from .models.dimension_based_attribute import DimensionBasedAttribute
from .models.duration_price import DurationPrice
from .models.error_data import ErrorData
from .models.external_ids import ExternalIds
from .models.get_browse_nodes_request import GetBrowseNodesRequest
from .models.get_browse_nodes_resource import GetBrowseNodesResource
from .models.get_browse_nodes_response import GetBrowseNodesResponse
from .models.get_items_request import GetItemsRequest
from .models.get_items_resource import GetItemsResource
from .models.get_items_response import GetItemsResponse
from .models.get_variations_request import GetVariationsRequest
from .models.get_variations_resource import GetVariationsResource
from .models.get_variations_response import GetVariationsResponse
from .models.hosts import Hosts
from .models.image_size import ImageSize
from .models.image_type import ImageType
from .models.images import Images
from .models.item import Item
from .models.item_id_type import ItemIdType
from .models.item_info import ItemInfo
from .models.items_result import ItemsResult
from .models.language_type import LanguageType
from .models.languages import Languages
from .models.locales import Locales
from .models.manufacture_info import ManufactureInfo
from .models.max_price import MaxPrice
from .models.merchant import Merchant
from .models.min_price import MinPrice
from .models.min_reviews_rating import MinReviewsRating
from .models.min_saving_percent import MinSavingPercent
from .models.money import Money
from .models.multi_valued_attribute import MultiValuedAttribute
from .models.offer_availability import OfferAvailability
from .models.offer_availability_v2 import OfferAvailabilityV2
from .models.offer_condition import OfferCondition
from .models.offer_condition_note import OfferConditionNote
from .models.offer_condition_v2 import OfferConditionV2
from .models.offer_count import OfferCount
from .models.offer_delivery_info import OfferDeliveryInfo
from .models.offer_listing import OfferListing
from .models.offer_listing_v2 import OfferListingV2
from .models.offer_listings import OfferListings
from .models.offer_listings_v2 import OfferListingsV2
from .models.offer_loyalty_points import OfferLoyaltyPoints
from .models.offer_loyalty_points_v2 import OfferLoyaltyPointsV2
from .models.offer_merchant_info import OfferMerchantInfo
from .models.offer_merchant_info_v2 import OfferMerchantInfoV2
from .models.offer_price import OfferPrice
from .models.offer_price_v2 import OfferPriceV2
from .models.offer_program_eligibility import OfferProgramEligibility
from .models.offer_promotion import OfferPromotion
from .models.offer_saving_basis import OfferSavingBasis
from .models.offer_savings import OfferSavings
from .models.offer_savings_v2 import OfferSavingsV2
from .models.offer_shipping_charge import OfferShippingCharge
from .models.offer_sub_condition import OfferSubCondition
from .models.offer_summary import OfferSummary
from .models.offer_type import OfferType
from .models.offers import Offers
from .models.offers_v2 import OffersV2
from .models.partner_type import PartnerType
from .models.price import Price
from .models.price_type import PriceType
from .models.product_info import ProductInfo
from .models.properties import Properties
from .models.rating import Rating
from .models.refinement import Refinement
from .models.refinement_bin import RefinementBin
from .models.regions import Regions
from .models.rental_offer_listing import RentalOfferListing
from .models.rental_offers import RentalOffers
from .models.saving_basis_type import SavingBasisType
from .models.search_index import SearchIndex
from .models.search_items_request import SearchItemsRequest
from .models.search_items_resource import SearchItemsResource
from .models.search_items_response import SearchItemsResponse
from .models.search_refinements import SearchRefinements
from .models.search_result import SearchResult
from .models.single_boolean_valued_attribute import SingleBooleanValuedAttribute
from .models.single_integer_valued_attribute import SingleIntegerValuedAttribute
from .models.single_string_valued_attribute import SingleStringValuedAttribute
from .models.sort_by import SortBy
from .models.targets import Targets
from .models.technical_info import TechnicalInfo
from .models.trade_in_info import TradeInInfo
from .models.trade_in_price import TradeInPrice
from .models.unit_based_attribute import UnitBasedAttribute
from .models.variation_attribute import VariationAttribute
from .models.variation_dimension import VariationDimension
from .models.variation_summary import VariationSummary
from .models.variations_result import VariationsResult
from .models.website_sales_rank import WebsiteSalesRank
from .transports import RequestDict, ResponseDict, Transport, AsyncTransport
from .utils import get_asin

# transports depends on its optional-dependencies
try:
    from .transports.use_requests import UseRequestsTransport
    from .transports.use_httpx import UseHttpxTransport
    from .transports.use_tornado import UseTornadoTransport
except ImportError:
    pass


__title__ = "amazon-paapi-python-sdk"
__description__ = "Amazon Product Advertising API 5.0 rewrited for Python."
__url__ = "https://github.com/mywaiting/amazon-paapi-python-sdk"
__author__ = "Heng<mywaiting>"
__email__ = "hi@mywaiting.com"
__copyright__ = "Copyright Mywaiting"