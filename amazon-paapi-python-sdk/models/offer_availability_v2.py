import dataclasses
import typing

@dataclasses.dataclass
class OfferAvailabilityV2:
    message: typing.Optional[str] = dataclasses.field(metadata={'key': 'Message'})
    max_order_quantity: typing.Optional[int] = dataclasses.field(metadata={'key': 'MaxOrderQuantity'})
    min_order_quantity: typing.Optional[int] = dataclasses.field(metadata={'key': 'MinOrderQuantity'})
    type: typing.Optional[str] = dataclasses.field(metadata={'key': 'Type'})