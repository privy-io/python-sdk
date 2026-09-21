# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .transfer_sca_outcome_param import TransferScaOutcomeParam
from .transfer_sca_auth_factor_param import TransferScaAuthFactorParam

__all__ = ["TransferScaAttestationParam"]


class TransferScaAttestationParam(TypedDict, total=False):
    """Strong Customer Authentication attestation for a transfer."""

    outcome: Required[TransferScaOutcomeParam]
    """
    Whether Strong Customer Authentication (SCA) was applied or which regulatory
    exemption or non-applicability reason covers this payment. Use `sca_used` when
    the user authenticated with SCA. Otherwise, choose the value that applies:
    `payment_to_self` — payer and payee are the same person (remote only);
    `trusted_beneficiaries` — payee is on the user's pre-approved list;
    `recurring_transaction` — amount and payee match a previously SCA-authorized
    recurring series; `contactless_low_value` — contactless card payment below the
    low-value threshold (non-remote only); `unattended_terminal_for_transport` —
    automated terminal for transport fares or parking (non-remote only); `low_value`
    — remote payment below the low-value threshold (remote only);
    `secure_corporate_payment` — dedicated corporate payment process with controls
    equivalent to SCA (remote only); `transaction_risk_analysis` — PSP has performed
    real-time risk analysis and the transaction falls within permitted thresholds
    (remote only); `merchant_initiated_transaction` — payment triggered by the
    merchant without the payer present, on a pre-authorized mandate (remote only);
    `not_applicable` — this flow requires initiation context but SCA and SCA
    exemptions do not apply; `other` — another recognized exemption not listed
    above.
    """

    auth_factors: Iterable[TransferScaAuthFactorParam]
    """Authentication factor metadata.

    Optional when `outcome` is `sca_used`; if provided, it must contain at least two
    entries from different `category` values (e.g. one `possession` factor and one
    `knowledge` factor). Omit this field for any other outcome.
    """
