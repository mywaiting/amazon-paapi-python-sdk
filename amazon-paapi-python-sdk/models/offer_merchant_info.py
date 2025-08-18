import dataclasses
import typing

@dataclasses.dataclass
class OfferMerchantInfo:
    default_shipping_country: typing.Optional[str] = dataclasses.field(metadata={'key': 'DefaultShippingCountry'})
    feedback_count: typing.Optional[int] = dataclasses.field(metadata={'key': 'FeedbackCount'})
    feedback_rating: typing.Optional[float] = dataclasses.field(metadata={'key': 'FeedbackRating'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})
    name: typing.Optional[str] = dataclasses.field(metadata={'key': 'Name'})