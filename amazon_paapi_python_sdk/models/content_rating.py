import dataclasses
import typing

from .single_string_valued_attribute import SingleStringValuedAttribute

@dataclasses.dataclass
class ContentRating:
    audience_rating: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'AudienceRating'})