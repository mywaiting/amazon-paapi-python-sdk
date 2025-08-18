import dataclasses
import typing

from .condition import Condition
from .item_id_type import ItemIdType
from .merchant import Merchant
from .offer_count import OfferCount
from .partner_type import PartnerType
from .properties import Properties
from .get_items_resource import GetItemsResource

@dataclasses.dataclass
class GetItemsRequest:
    condition: typing.Optional[Condition] = dataclasses.field(metadata={'key': 'Condition'})
    currency_of_preference: typing.Optional[str] = dataclasses.field(metadata={'key': 'CurrencyOfPreference'})
    item_ids: typing.Optional[list[str]] = dataclasses.field(metadata={'key': 'ItemIds'})
    item_id_type: typing.Optional[ItemIdType] = dataclasses.field(metadata={'key': 'ItemIdType'})
    languages_of_preference: typing.Optional[list[str]] = dataclasses.field(metadata={'key': 'LanguagesOfPreference'})
    marketplace: typing.Optional[str] = dataclasses.field(metadata={'key': 'Marketplace'})
    merchant: typing.Optional[Merchant] = dataclasses.field(metadata={'key': 'Merchant'})
    offer_count: typing.Optional[OfferCount] = dataclasses.field(metadata={'key': 'OfferCount'})
    partner_tag: typing.Optional[str] = dataclasses.field(metadata={'key': 'PartnerTag'})
    partner_type: typing.Optional[PartnerType] = dataclasses.field(metadata={'key': 'PartnerType'})
    properties: typing.Optional[Properties] = dataclasses.field(metadata={'key': 'Properties'})
    resources: typing.Optional[list[GetItemsResource]] = dataclasses.field(metadata={'key': 'Resources'})