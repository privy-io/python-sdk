# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

from .sui_command_name import SuiCommandName
from .sui_transaction_command_operator import SuiTransactionCommandOperator

__all__ = ["SuiTransactionCommandConditionParam"]


class SuiTransactionCommandConditionParam(TypedDict, total=False):
    """SUI transaction command attributes, enables allowlisting specific command types.

    Allowed commands: 'TransferObjects', 'SplitCoins', 'MergeCoins'. Only 'eq' and 'in' operators are supported.
    """

    field: Required[Literal["commandName"]]

    field_source: Required[Literal["sui_transaction_command"]]

    operator: Required[SuiTransactionCommandOperator]
    """Operator to use for SUI transaction command conditions.

    Only 'eq' and 'in' are supported for command names.
    """

    value: Required[Union[SuiCommandName, List[SuiCommandName]]]
    """Command name(s) to match.

    Must be one of: 'TransferObjects', 'SplitCoins', 'MergeCoins'
    """
