# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .privy_fee import PrivyFee
from .relayer_fee import RelayerFee
from .developer_fee import DeveloperFee

__all__ = ["FeeLineItem"]

FeeLineItem: TypeAlias = Annotated[Union[RelayerFee, PrivyFee, DeveloperFee], PropertyInfo(discriminator="type")]
