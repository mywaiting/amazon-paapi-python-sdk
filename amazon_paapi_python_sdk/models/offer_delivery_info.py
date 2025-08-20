import dataclasses
import typing

from .offer_shipping_charge import OfferShippingCharge

@dataclasses.dataclass
class OfferDeliveryInfo:
    is_amazon_fulfilled: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsAmazonFulfilled'})
    is_free_shipping_eligible: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsFreeShippingEligible'})
    is_prime_eligible: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsPrimeEligible'})
    shipping_charges: typing.Optional[list[OfferShippingCharge]] = dataclasses.field(metadata={'key': 'ShippingCharges'})