import dataclasses
import typing

@dataclasses.dataclass
class OfferProgramEligibility:
    is_prime_exclusive: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsPrimeExclusive'})
    is_prime_pantry: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsPrimePantry'})