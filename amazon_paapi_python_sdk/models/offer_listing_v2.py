import dataclasses
import typing

from .offer_availability_v2 import OfferAvailabilityV2
from .offer_condition_v2 import OfferConditionV2
from .deal_details import DealDetails
from .offer_loyalty_points_v2 import OfferLoyaltyPointsV2
from .offer_merchant_info_v2 import OfferMerchantInfoV2
from .offer_price_v2 import OfferPriceV2
from .offer_type import OfferType

@dataclasses.dataclass
class OfferListingV2:
    availability: typing.Optional[OfferAvailabilityV2] = dataclasses.field(metadata={'key': 'Availability'})
    condition: typing.Optional[OfferConditionV2] = dataclasses.field(metadata={'key': 'Condition'})
    deal_details: typing.Optional[DealDetails] = dataclasses.field(metadata={'key': 'DealDetails'})
    is_buy_box_winner: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsBuyBoxWinner'})
    loyalty_points: typing.Optional[OfferLoyaltyPointsV2] = dataclasses.field(metadata={'key': 'LoyaltyPoints'})
    merchant_info: typing.Optional[OfferMerchantInfoV2] = dataclasses.field(metadata={'key': 'MerchantInfo'})
    price: typing.Optional[OfferPriceV2] = dataclasses.field(metadata={'key': 'Price'})
    type: typing.Optional[OfferType] = dataclasses.field(metadata={'key': 'Type'})
    violates_map: typing.Optional[bool] = dataclasses.field(metadata={'key': 'ViolatesMAP'})