# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .aave_vault_details import AaveVaultDetails
from .veda_vault_details import VedaVaultDetails
from .tempo_vault_details import TempoVaultDetails
from .morpho_vault_details import MorphoVaultDetails

__all__ = ["EthereumEarnVaultDetailsResponse"]

EthereumEarnVaultDetailsResponse: TypeAlias = Annotated[
    Union[AaveVaultDetails, MorphoVaultDetails, TempoVaultDetails, VedaVaultDetails],
    PropertyInfo(discriminator="provider"),
]
