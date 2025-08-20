import dataclasses
import typing

from .partner_type import PartnerType
from .get_browse_nodes_resource import GetBrowseNodesResource

@dataclasses.dataclass
class GetBrowseNodesRequest:
    browse_node_ids: typing.Optional[list[str]] = dataclasses.field(metadata={'key': 'BrowseNodeIds'})
    languages_of_preference: typing.Optional[list[str]] = dataclasses.field(metadata={'key': 'LanguagesOfPreference'})
    marketplace: typing.Optional[str] = dataclasses.field(metadata={'key': 'Marketplace'})
    partner_tag: typing.Optional[str] = dataclasses.field(metadata={'key': 'PartnerTag'})
    partner_type: typing.Optional[PartnerType] = dataclasses.field(metadata={'key': 'PartnerType'})
    resources: typing.Optional[list[GetBrowseNodesResource]] = dataclasses.field(metadata={'key': 'Resources'})