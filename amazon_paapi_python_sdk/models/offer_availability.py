import dataclasses
import typing

@dataclasses.dataclass
class OfferAvailability:
    max_order_quantity: typing.Optional[int] = dataclasses.field(metadata={'key': 'MaxOrderQuantity'})
    message: typing.Optional[str] = dataclasses.field(metadata={'key': 'Message'})
    min_order_quantity: typing.Optional[int] = dataclasses.field(metadata={'key': 'MinOrderQuantity'})
    type: typing.Optional[str] = dataclasses.field(metadata={'key': 'Type'})