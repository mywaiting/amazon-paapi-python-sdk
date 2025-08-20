import dataclasses
import typing

@dataclasses.dataclass
class OfferShippingCharge:
    amount: typing.Optional[float] = dataclasses.field(metadata={'key': 'Amount'})
    currency: typing.Optional[str] = dataclasses.field(metadata={'key': 'Currency'})
    display_amount: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayAmount'})
    is_rate_tax_inclusive: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsRateTaxInclusive'})
    type: typing.Optional[str] = dataclasses.field(metadata={'key': 'Type'})