import dataclasses
import typing

from .money import Money
from .saving_basis_type import SavingBasisType

@dataclasses.dataclass
class OfferSavingBasis:
    money: typing.Optional[Money] = dataclasses.field(metadata={'key': 'Money'})
    saving_basis_type: typing.Optional[SavingBasisType] = dataclasses.field(metadata={'key': 'SavingBasisType'})
    saving_basis_type_label: typing.Optional[str] = dataclasses.field(metadata={'key': 'SavingBasisTypeLabel'})