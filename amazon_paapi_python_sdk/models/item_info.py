import dataclasses
import typing

from .by_line_info import ByLineInfo
from .classifications import Classifications
from .content_info import ContentInfo
from .content_rating import ContentRating
from .external_ids import ExternalIds
from .multi_valued_attribute import MultiValuedAttribute
from .manufacture_info import ManufactureInfo
from .product_info import ProductInfo
from .technical_info import TechnicalInfo
from .single_string_valued_attribute import SingleStringValuedAttribute
from .trade_in_info import TradeInInfo

@dataclasses.dataclass
class ItemInfo:
    by_line_info: typing.Optional[ByLineInfo] = dataclasses.field(metadata={'key': 'ByLineInfo'})
    classifications: typing.Optional[Classifications] = dataclasses.field(metadata={'key': 'Classifications'})
    content_info: typing.Optional[ContentInfo] = dataclasses.field(metadata={'key': 'ContentInfo'})
    content_rating: typing.Optional[ContentRating] = dataclasses.field(metadata={'key': 'ContentRating'})
    external_ids: typing.Optional[ExternalIds] = dataclasses.field(metadata={'key': 'ExternalIds'})
    features: typing.Optional[MultiValuedAttribute] = dataclasses.field(metadata={'key': 'Features'})
    manufacture_info: typing.Optional[ManufactureInfo] = dataclasses.field(metadata={'key': 'ManufactureInfo'})
    product_info: typing.Optional[ProductInfo] = dataclasses.field(metadata={'key': 'ProductInfo'})
    technical_info: typing.Optional[TechnicalInfo] = dataclasses.field(metadata={'key': 'TechnicalInfo'})
    title: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Title'})
    trade_in_info: typing.Optional[TradeInInfo] = dataclasses.field(metadata={'key': 'TradeInInfo'})