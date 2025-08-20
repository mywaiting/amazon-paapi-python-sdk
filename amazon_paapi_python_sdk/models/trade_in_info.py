import dataclasses
import typing

from .trade_in_price import TradeInPrice

@dataclasses.dataclass
class TradeInInfo:
    is_eligible_for_trade_in: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsEligibleForTradeIn'})
    price: typing.Optional[TradeInPrice] = dataclasses.field(metadata={'key': 'Price'})