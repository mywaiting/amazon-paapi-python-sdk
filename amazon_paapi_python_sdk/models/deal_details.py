import dataclasses
import typing

@dataclasses.dataclass
class DealDetails:
    access_type: typing.Optional[str] = dataclasses.field(metadata={'key': 'AccessType'})
    badge: typing.Optional[str] = dataclasses.field(metadata={'key': 'Badge'})
    early_access_duration_in_milliseconds: typing.Optional[int] = dataclasses.field(metadata={'key': 'EarlyAccessDurationInMilliseconds'})
    end_time: typing.Optional[str] = dataclasses.field(metadata={'key': 'EndTime'})
    percent_claimed: typing.Optional[int] = dataclasses.field(metadata={'key': 'PercentClaimed'})
    start_time: typing.Optional[str] = dataclasses.field(metadata={'key': 'StartTime'})