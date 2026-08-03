# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from .._models import BaseModel
from .sui_command_name import SuiCommandName
from .sui_transaction_command_operator import SuiTransactionCommandOperator

__all__ = ["SuiTransactionCommandCondition"]


class SuiTransactionCommandCondition(BaseModel):
    """SUI transaction command attributes, enables allowlisting specific command types.

    Allowed commands: 'TransferObjects', 'SplitCoins', 'MergeCoins'. Only 'eq' and 'in' operators are supported.
    """

    field: Literal["commandName"]

    field_source: Literal["sui_transaction_command"]

    operator: SuiTransactionCommandOperator
    """Operator to use for SUI transaction command conditions.

    Only 'eq' and 'in' are supported for command names.
    """

    value: Union[SuiCommandName, List[SuiCommandName]]
    """Command name(s) to match.

    Must be one of: 'TransferObjects', 'SplitCoins', 'MergeCoins'
    """
