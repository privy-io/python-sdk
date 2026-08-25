# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .mfa_enabled_webhook_payload import MfaEnabledWebhookPayload
from .mfa_disabled_webhook_payload import MfaDisabledWebhookPayload
from .user_created_webhook_payload import UserCreatedWebhookPayload
from .user_deleted_webhook_payload import UserDeletedWebhookPayload
from .intent_failed_webhook_payload import IntentFailedWebhookPayload
from .intent_created_webhook_payload import IntentCreatedWebhookPayload
from .user_kyc_updated_webhook_event import UserKYCUpdatedWebhookEvent
from .funds_deposited_webhook_payload import FundsDepositedWebhookPayload
from .funds_withdrawn_webhook_payload import FundsWithdrawnWebhookPayload
from .intent_executed_webhook_payload import IntentExecutedWebhookPayload
from .intent_rejected_webhook_payload import IntentRejectedWebhookPayload
from .wallet_archived_webhook_payload import WalletArchivedWebhookPayload
from .wallet_restored_webhook_payload import WalletRestoredWebhookPayload
from .wallet_recovered_webhook_payload import WalletRecoveredWebhookPayload
from .intent_authorized_webhook_payload import IntentAuthorizedWebhookPayload
from .private_key_export_webhook_payload import PrivateKeyExportWebhookPayload
from .transaction_failed_webhook_payload import TransactionFailedWebhookPayload
from .user_authenticated_webhook_payload import UserAuthenticatedWebhookPayload
from .user_linked_account_webhook_payload import UserLinkedAccountWebhookPayload
from .user_wallet_created_webhook_payload import UserWalletCreatedWebhookPayload
from .transaction_replaced_webhook_payload import TransactionReplacedWebhookPayload
from .user_updated_account_webhook_payload import UserUpdatedAccountWebhookPayload
from .transaction_confirmed_webhook_payload import TransactionConfirmedWebhookPayload
from .user_unlinked_account_webhook_payload import UserUnlinkedAccountWebhookPayload
from .wallet_recovery_setup_webhook_payload import WalletRecoverySetupWebhookPayload
from .yield_claim_confirmed_webhook_payload import YieldClaimConfirmedWebhookPayload
from .organization_kyb_updated_webhook_event import OrganizationKYBUpdatedWebhookEvent
from .transaction_broadcasted_webhook_payload import TransactionBroadcastedWebhookPayload
from .yield_deposit_confirmed_webhook_payload import YieldDepositConfirmedWebhookPayload
from .user_operation_completed_webhook_payload import UserOperationCompletedWebhookPayload
from .user_transferred_account_webhook_payload import UserTransferredAccountWebhookPayload
from .yield_withdraw_confirmed_webhook_payload import YieldWithdrawConfirmedWebhookPayload
from .transaction_still_pending_webhook_payload import TransactionStillPendingWebhookPayload
from .wallet_action_swap_failed_webhook_payload import WalletActionSwapFailedWebhookPayload
from .transaction_provider_error_webhook_payload import TransactionProviderErrorWebhookPayload
from .wallet_action_swap_created_webhook_payload import WalletActionSwapCreatedWebhookPayload
from .wallet_action_payout_failed_webhook_payload import WalletActionPayoutFailedWebhookPayload
from .wallet_action_swap_rejected_webhook_payload import WalletActionSwapRejectedWebhookPayload
from .wallet_automation_submitted_webhook_payload import WalletAutomationSubmittedWebhookPayload
from .wallet_action_payout_created_webhook_payload import WalletActionPayoutCreatedWebhookPayload
from .wallet_action_swap_succeeded_webhook_payload import WalletActionSwapSucceededWebhookPayload
from .wallet_action_payout_rejected_webhook_payload import WalletActionPayoutRejectedWebhookPayload
from .wallet_action_transfer_failed_webhook_payload import WalletActionTransferFailedWebhookPayload
from .transaction_execution_reverted_webhook_payload import TransactionExecutionRevertedWebhookPayload
from .usage_cross_chain_fee_recorded_webhook_payload import UsageCrossChainFeeRecordedWebhookPayload
from .usage_gas_sponsorship_recorded_webhook_payload import UsageGasSponsorshipRecordedWebhookPayload
from .wallet_action_payout_succeeded_webhook_payload import WalletActionPayoutSucceededWebhookPayload
from .wallet_action_transfer_created_webhook_payload import WalletActionTransferCreatedWebhookPayload
from .wallet_action_transfer_rejected_webhook_payload import WalletActionTransferRejectedWebhookPayload
from .wallet_action_transfer_succeeded_webhook_payload import WalletActionTransferSucceededWebhookPayload
from .wallet_action_earn_deposit_failed_webhook_payload import WalletActionEarnDepositFailedWebhookPayload
from .wallet_action_earn_deposit_created_webhook_payload import WalletActionEarnDepositCreatedWebhookPayload
from .wallet_action_earn_withdraw_failed_webhook_payload import WalletActionEarnWithdrawFailedWebhookPayload
from .wallet_action_earn_deposit_rejected_webhook_payload import WalletActionEarnDepositRejectedWebhookPayload
from .wallet_action_earn_withdraw_created_webhook_payload import WalletActionEarnWithdrawCreatedWebhookPayload
from .wallet_deposit_account_deposit_failed_webhook_event import WalletDepositAccountDepositFailedWebhookEvent
from .wallet_action_earn_deposit_succeeded_webhook_payload import WalletActionEarnDepositSucceededWebhookPayload
from .wallet_action_earn_withdraw_rejected_webhook_payload import WalletActionEarnWithdrawRejectedWebhookPayload
from .wallet_deposit_account_deposit_started_webhook_event import WalletDepositAccountDepositStartedWebhookEvent
from .wallet_action_earn_fee_collect_failed_webhook_payload import WalletActionEarnFeeCollectFailedWebhookPayload
from .wallet_action_earn_withdraw_succeeded_webhook_payload import WalletActionEarnWithdrawSucceededWebhookPayload
from .wallet_action_earn_fee_collect_created_webhook_payload import WalletActionEarnFeeCollectCreatedWebhookPayload
from .wallet_deposit_account_deposit_completed_webhook_event import WalletDepositAccountDepositCompletedWebhookEvent
from .wallet_action_earn_fee_collect_rejected_webhook_payload import WalletActionEarnFeeCollectRejectedWebhookPayload
from .wallet_action_earn_fee_collect_succeeded_webhook_payload import WalletActionEarnFeeCollectSucceededWebhookPayload
from .wallet_action_earn_incentive_claim_failed_webhook_payload import (
    WalletActionEarnIncentiveClaimFailedWebhookPayload,
)
from .wallet_action_earn_incentive_claim_created_webhook_payload import (
    WalletActionEarnIncentiveClaimCreatedWebhookPayload,
)
from .wallet_action_earn_incentive_claim_rejected_webhook_payload import (
    WalletActionEarnIncentiveClaimRejectedWebhookPayload,
)
from .wallet_action_earn_incentive_claim_succeeded_webhook_payload import (
    WalletActionEarnIncentiveClaimSucceededWebhookPayload,
)

__all__ = ["UnsafeUnwrapWebhookEvent"]

UnsafeUnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        IntentAuthorizedWebhookPayload,
        IntentCreatedWebhookPayload,
        IntentExecutedWebhookPayload,
        IntentFailedWebhookPayload,
        IntentRejectedWebhookPayload,
        MfaDisabledWebhookPayload,
        MfaEnabledWebhookPayload,
        OrganizationKYBUpdatedWebhookEvent,
        TransactionBroadcastedWebhookPayload,
        TransactionConfirmedWebhookPayload,
        TransactionExecutionRevertedWebhookPayload,
        TransactionFailedWebhookPayload,
        TransactionProviderErrorWebhookPayload,
        TransactionReplacedWebhookPayload,
        TransactionStillPendingWebhookPayload,
        UsageCrossChainFeeRecordedWebhookPayload,
        UsageGasSponsorshipRecordedWebhookPayload,
        UserAuthenticatedWebhookPayload,
        UserCreatedWebhookPayload,
        UserDeletedWebhookPayload,
        UserKYCUpdatedWebhookEvent,
        UserLinkedAccountWebhookPayload,
        UserTransferredAccountWebhookPayload,
        UserUnlinkedAccountWebhookPayload,
        UserUpdatedAccountWebhookPayload,
        UserWalletCreatedWebhookPayload,
        UserOperationCompletedWebhookPayload,
        WalletArchivedWebhookPayload,
        WalletDepositAccountDepositCompletedWebhookEvent,
        WalletDepositAccountDepositFailedWebhookEvent,
        WalletDepositAccountDepositStartedWebhookEvent,
        FundsDepositedWebhookPayload,
        FundsWithdrawnWebhookPayload,
        PrivateKeyExportWebhookPayload,
        WalletRecoveredWebhookPayload,
        WalletRecoverySetupWebhookPayload,
        WalletRestoredWebhookPayload,
        WalletActionEarnDepositCreatedWebhookPayload,
        WalletActionEarnDepositFailedWebhookPayload,
        WalletActionEarnDepositRejectedWebhookPayload,
        WalletActionEarnDepositSucceededWebhookPayload,
        WalletActionEarnFeeCollectCreatedWebhookPayload,
        WalletActionEarnFeeCollectFailedWebhookPayload,
        WalletActionEarnFeeCollectRejectedWebhookPayload,
        WalletActionEarnFeeCollectSucceededWebhookPayload,
        WalletActionEarnIncentiveClaimCreatedWebhookPayload,
        WalletActionEarnIncentiveClaimFailedWebhookPayload,
        WalletActionEarnIncentiveClaimRejectedWebhookPayload,
        WalletActionEarnIncentiveClaimSucceededWebhookPayload,
        WalletActionEarnWithdrawCreatedWebhookPayload,
        WalletActionEarnWithdrawFailedWebhookPayload,
        WalletActionEarnWithdrawRejectedWebhookPayload,
        WalletActionEarnWithdrawSucceededWebhookPayload,
        WalletActionPayoutCreatedWebhookPayload,
        WalletActionPayoutFailedWebhookPayload,
        WalletActionPayoutRejectedWebhookPayload,
        WalletActionPayoutSucceededWebhookPayload,
        WalletActionSwapCreatedWebhookPayload,
        WalletActionSwapFailedWebhookPayload,
        WalletActionSwapRejectedWebhookPayload,
        WalletActionSwapSucceededWebhookPayload,
        WalletActionTransferCreatedWebhookPayload,
        WalletActionTransferFailedWebhookPayload,
        WalletActionTransferRejectedWebhookPayload,
        WalletActionTransferSucceededWebhookPayload,
        WalletAutomationSubmittedWebhookPayload,
        YieldClaimConfirmedWebhookPayload,
        YieldDepositConfirmedWebhookPayload,
        YieldWithdrawConfirmedWebhookPayload,
    ],
    PropertyInfo(discriminator="type"),
]
