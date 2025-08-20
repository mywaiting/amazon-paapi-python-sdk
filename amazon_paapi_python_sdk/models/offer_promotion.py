import dataclasses
import typing

@dataclasses.dataclass
class OfferPromotion:
    amount: typing.Optional[float] = dataclasses.field(metadata={'key': 'Amount'})
    currency: typing.Optional[str] = dataclasses.field(metadata={'key': 'Currency'})
    discount_percent: typing.Optional[int] = dataclasses.field(metadata={'key': 'DiscountPercent'})
    display_amount: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayAmount'})
    price_per_unit: typing.Optional[float] = dataclasses.field(metadata={'key': 'PricePerUnit'})
    type: typing.Optional[str] = dataclasses.field(metadata={'key': 'Type'})