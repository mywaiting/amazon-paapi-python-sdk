import dataclasses
import typing

@dataclasses.dataclass
class OfferConditionV2:
    value: typing.Optional[str] = dataclasses.field(metadata={'key': 'Value'})
    sub_condition: typing.Optional[str] = dataclasses.field(metadata={'key': 'SubCondition'})
    condition_note: typing.Optional[str] = dataclasses.field(metadata={'key': 'ConditionNote'})