# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .additional_signer_item_input import AdditionalSignerItemInput

__all__ = ["AdditionalSignerInput"]

AdditionalSignerInput: TypeAlias = List[AdditionalSignerItemInput]
