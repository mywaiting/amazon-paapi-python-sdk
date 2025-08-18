import dataclasses
import typing

@dataclasses.dataclass
class OfferMerchantInfoV2:
    name: typing.Optional[str] = dataclasses.field(metadata={'key': 'Name'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})