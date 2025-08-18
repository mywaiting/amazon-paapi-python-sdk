import dataclasses
import typing

from .offer_availability import OfferAvailability
from .duration_price import DurationPrice
from .offer_condition import OfferCondition
from .offer_delivery_info import OfferDeliveryInfo
from .offer_merchant_info import OfferMerchantInfo

@dataclasses.dataclass
class RentalOfferListing:
    availability: typing.Optional[OfferAvailability] = dataclasses.field(metadata={'key': 'Availability'})
    base_price: typing.Optional[DurationPrice] = dataclasses.field(metadata={'key': 'BasePrice'})
    condition: typing.Optional[OfferCondition] = dataclasses.field(metadata={'key': 'Condition'})
    delivery_info: typing.Optional[OfferDeliveryInfo] = dataclasses.field(metadata={'key': 'DeliveryInfo'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})
    merchant_info: typing.Optional[OfferMerchantInfo] = dataclasses.field(metadata={'key': 'MerchantInfo'})