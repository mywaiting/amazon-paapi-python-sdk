import dataclasses
import typing

@dataclasses.dataclass
class TradeInPrice:
    amount: typing.Optional[float] = dataclasses.field(metadata={'key': 'Amount'})
    currency: typing.Optional[str] = dataclasses.field(metadata={'key': 'Currency'})
    display_amount: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayAmount'})