import dataclasses
import typing

from .offer_availability import OfferAvailability
from .offer_condition import OfferCondition
from .offer_delivery_info import OfferDeliveryInfo
from .offer_loyalty_points import OfferLoyaltyPoints
from .offer_merchant_info import OfferMerchantInfo
from .offer_price import OfferPrice
from .offer_program_eligibility import OfferProgramEligibility
from .offer_promotion import OfferPromotion

@dataclasses.dataclass
class OfferListing:
    availability: typing.Optional[OfferAvailability] = dataclasses.field(metadata={'key': 'Availability'})
    condition: typing.Optional[OfferCondition] = dataclasses.field(metadata={'key': 'Condition'})
    delivery_info: typing.Optional[OfferDeliveryInfo] = dataclasses.field(metadata={'key': 'DeliveryInfo'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})
    is_buy_box_winner: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsBuyBoxWinner'})
    loyalty_points: typing.Optional[OfferLoyaltyPoints] = dataclasses.field(metadata={'key': 'LoyaltyPoints'})
    merchant_info: typing.Optional[OfferMerchantInfo] = dataclasses.field(metadata={'key': 'MerchantInfo'})
    price: typing.Optional[OfferPrice] = dataclasses.field(metadata={'key': 'Price'})
    program_eligibility: typing.Optional[OfferProgramEligibility] = dataclasses.field(metadata={'key': 'ProgramEligibility'})
    promotions: typing.Optional[list[OfferPromotion]] = dataclasses.field(metadata={'key': 'Promotions'})
    saving_basis: typing.Optional[OfferPrice] = dataclasses.field(metadata={'key': 'SavingBasis'})
    violates_map: typing.Optional[bool] = dataclasses.field(metadata={'key': 'ViolatesMAP'})