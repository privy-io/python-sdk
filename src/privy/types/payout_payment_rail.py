# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PayoutPaymentRail"]

PayoutPaymentRail: TypeAlias = Literal["ach", "ach_same_day", "wire", "fednow", "sepa", "faster_payments", "pix"]
