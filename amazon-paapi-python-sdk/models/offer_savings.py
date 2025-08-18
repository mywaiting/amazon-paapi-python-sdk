import dataclasses
import typing

@dataclasses.dataclass
class OfferSavings:
    amount: typing.Optional[float] = dataclasses.field(metadata={'key': 'Amount'})
    currency: typing.Optional[str] = dataclasses.field(metadata={'key': 'Currency'})
    display_amount: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayAmount'})
    percentage: typing.Optional[int] = dataclasses.field(metadata={'key': 'Percentage'})
    price_per_unit: typing.Optional[float] = dataclasses.field(metadata={'key': 'PricePerUnit'})