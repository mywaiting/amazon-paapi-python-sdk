import dataclasses
import typing

from .big_decimal import BigDecimal

@dataclasses.dataclass
class Money:
    amount: typing.Optional[BigDecimal] = dataclasses.field(metadata={'key': 'Amount'})
    currency: typing.Optional[str] = dataclasses.field(metadata={'key': 'Currency'})
    display_amount: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayAmount'})