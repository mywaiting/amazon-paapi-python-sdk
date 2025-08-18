import dataclasses
import typing

from .single_string_valued_attribute import SingleStringValuedAttribute
from .single_integer_valued_attribute import SingleIntegerValuedAttribute
from .languages import Languages

@dataclasses.dataclass
class ContentInfo:
    edition: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Edition'})
    languages: typing.Optional[Languages] = dataclasses.field(metadata={'key': 'Languages'})
    pages_count: typing.Optional[SingleIntegerValuedAttribute] = dataclasses.field(metadata={'key': 'PagesCount'})
    publication_date: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'PublicationDate'})