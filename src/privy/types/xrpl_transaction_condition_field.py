# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["XrplTransactionConditionField"]

XrplTransactionConditionField: TypeAlias = Literal[
    "TransactionType",
    "Payment.Destination",
    "Payment.DestinationTag",
    "Payment.Amount.drops",
    "Payment.Amount.value",
    "Payment.Amount.currency",
    "Payment.Amount.issuer",
    "Payment.SendMax.drops",
    "Payment.SendMax.value",
    "Payment.SendMax.currency",
    "Payment.SendMax.issuer",
    "Payment.DeliverMin.drops",
    "Payment.DeliverMin.value",
    "Payment.DeliverMin.currency",
    "Payment.DeliverMin.issuer",
    "OfferCreate.TakerPays.drops",
    "OfferCreate.TakerPays.value",
    "OfferCreate.TakerPays.currency",
    "OfferCreate.TakerPays.issuer",
    "OfferCreate.TakerGets.drops",
    "OfferCreate.TakerGets.value",
    "OfferCreate.TakerGets.currency",
    "OfferCreate.TakerGets.issuer",
    "OfferCreate.Expiration",
    "TrustSet.LimitAmount.value",
    "TrustSet.LimitAmount.currency",
    "TrustSet.LimitAmount.issuer",
    "TrustSet.QualityIn",
    "TrustSet.QualityOut",
]
