# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FiatPaymentRail"]

FiatPaymentRail: TypeAlias = Literal["sepa", "ach_push", "wire", "fednow", "faster_payments"]
