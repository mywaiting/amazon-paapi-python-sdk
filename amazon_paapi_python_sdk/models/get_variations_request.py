import dataclasses
import typing

from .condition import Condition
from .merchant import Merchant
from .offer_count import OfferCount
from .partner_type import PartnerType
from .properties import Properties
from .get_variations_resource import GetVariationsResource

@dataclasses.dataclass
class GetVariationsRequest:
    asin: typing.Optional[str] = dataclasses.field(metadata={'key': 'ASIN'})
    condition: typing.Optional[Condition] = dataclasses.field(metadata={'key': 'Condition'})
    currency_of_preference: typing.Optional[str] = dataclasses.field(metadata={'key': 'CurrencyOfPreference'})
    languages_of_preference: typing.Optional[list[str]] = dataclasses.field(metadata={'key': 'LanguagesOfPreference'})
    marketplace: typing.Optional[str] = dataclasses.field(metadata={'key': 'Marketplace'})
    merchant: typing.Optional[Merchant] = dataclasses.field(metadata={'key': 'Merchant'})
    offer_count: typing.Optional[OfferCount] = dataclasses.field(metadata={'key': 'OfferCount'})
    partner_tag: typing.Optional[str] = dataclasses.field(metadata={'key': 'PartnerTag'})
    partner_type: typing.Optional[PartnerType] = dataclasses.field(metadata={'key': 'PartnerType'})
    properties: typing.Optional[Properties] = dataclasses.field(metadata={'key': 'Properties'})
    resources: typing.Optional[list[GetVariationsResource]] = dataclasses.field(metadata={'key': 'Resources'})
    variation_count: typing.Optional[int] = dataclasses.field(metadata={'key': 'VariationCount'})
    variation_page: typing.Optional[int] = dataclasses.field(metadata={'key': 'VariationPage'})