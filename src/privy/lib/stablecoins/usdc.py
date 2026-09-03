from typing import Literal, cast

from .erc20 import build_usdc_transfer_data
from ..._client import PrivyAPI
from .constants import BRIDGE_CHAIN_NAMES, USDC_CONTRACT_ADDRESSES
from ...types.fiat import (
    OnrampCreateResponse,
    onramp_create_params,
    offramp_create_params,
)
from ...types.wallet_rpc_params import (
    EthSendTransactionParams,
    EthSendTransactionParamsTransaction,
)
from ...types.wallet_rpc_response import EthSendTransaction, EthSendTransactionData

# Type for supported bridge chains
BridgeChain = Literal["ethereum", "base", "arbitrum", "polygon", "optimism"]


def send_usdc(
    client: PrivyAPI,
    wallet_id: str,
    recipient_address: str,
    amount_in_usdc: float,
    chain_id: int = 8453,
) -> EthSendTransactionData:
    """Helper function to send USDC from a user's wallet to a specified address. By default, this function sends USDC to Base mainnet.

    Args:
        client: The Privy client instance
        wallet_id: The Privy wallet ID of the wallet sending the USDC
        recipient_address: The address to send USDC to
        amount_in_usdc: The amount of USDC to send (in USDC units, not wei)
        chain_id: The chain ID of the chain to send USDC from (default is Base mainnet)

    Returns:
        EthSendTransactionData: The transaction data of the USDC transfer

    Raises:
        ValueError: If the amount is invalid or the wallet doesn't have enough USDC
        RuntimeError: If the USDC transfer fails
    """
    # Get the USDC contract address for the specified chain
    usdc_address = USDC_CONTRACT_ADDRESSES[chain_id]

    # Build the USDC transfer data
    transfer_data = build_usdc_transfer_data(
        recipient_address=recipient_address,
        amount_usdc=float(amount_in_usdc),
        chain_id=chain_id,
    )

    # Send USDC to the target address
    rpc_response = cast(
        EthSendTransaction,
        client.wallets.rpc(
            wallet_id=wallet_id,
            method="eth_sendTransaction",
            params=EthSendTransactionParams(
                transaction=EthSendTransactionParamsTransaction(
                    to=usdc_address,
                    # Note: The recipient address is not used here, as the transfer is done via the contract
                    # The recipient is specified in the transfer data
                    value="0x0",  # For USDC transfers, value should be 0
                    data=transfer_data,
                    chain_id=chain_id,
                ),
            ),
            chain_type="ethereum",
            caip2=f"eip155:{chain_id}",
        ),
    )

    if rpc_response.data is None:
        raise RuntimeError("Failed to get transaction data")
    return rpc_response.data


def deposit_usdc_from_bank(
    client: PrivyAPI,
    user_id: str,
    wallet_id: str,
    amount_in_usdc: float,
    onramp_source: onramp_create_params.Source,
    onramp_provider: Literal["bridge", "bridge-sandbox"],
    chain_id: int = 8453,
) -> OnrampCreateResponse:
    """Helper function to handle the complete onramp flow from a bank account into a user's wallet. By default, this function onramp USDC to Base mainnet.

    Args:
        client: The Privy client instance
        user_id: The Privy user ID of the user initiating the onramp
        wallet_id: The Privy wallet ID of the wallet to receive the USDC
        amount_in_usdc: The amount of USDC to onramp (in USDC units, not wei)
        onramp_source: The source details for the onramp (e.g., bank account)
        onramp_provider: The provider to use for the onramp ("bridge" for production, "bridge-sandbox" for testing)
        chain_id: The chain ID of the chain to onramp USDC to (default is Base mainnet)

    Returns:
        OnrampCreateResponse containing the onramp details and status

    Raises:
        ValueError: If the amount is invalid
        RuntimeError: If the onramp request fails
    """
    # Convert the chain ID to a bridge chain name
    chain = cast(BridgeChain, BRIDGE_CHAIN_NAMES[chain_id])

    # Get the wallet
    wallet = client.wallets.get(wallet_id)

    onramp_destination = onramp_create_params.Destination(
        chain=chain,
        currency="usdc",
        to_address=wallet.address,
    )

    onramp_response = client.fiat.onramp.create(
        user_id=user_id,
        amount=str(amount_in_usdc),
        destination=onramp_destination,
        provider=onramp_provider,
        source=onramp_source,
    )

    return onramp_response


def withdraw_usdc_to_bank(
    client: PrivyAPI,
    user_id: str,
    wallet_id: str,
    amount_in_usdc: float,
    offramp_destination: offramp_create_params.Destination,
    offramp_provider: Literal["bridge", "bridge-sandbox"],
    chain_id: int = 8453,
) -> EthSendTransactionData:
    """Helper function to handle the complete offramp flow including USDC transfer from a user's wallet into a bank account. By default, this function offramp USDC from Base mainnet.

    Args:
        client: The Privy client instance
        user_id: The Privy user ID of the user initiating the offramp
        wallet_id: The Privy ID of the wallet containing the USDC to offramp
        amount_in_usdc: The amount of USDC to offramp (in USDC units, not wei)
        offramp_destination: The destination details for the offramp (e.g., bank account)
        offramp_provider: The provider to use for the offramp ("bridge" for production, "bridge-sandbox" for testing)
        chain_id: The chain ID of the chain to offramp USDC from (default is Base mainnet)

    Returns:
        EthSendTransactionData: The transaction data of the USDC transfer

    Raises:
        ValueError: If the amount is invalid or the wallet doesn't have enough USDC
        RuntimeError: If the offramp request fails or the USDC transfer fails
    """
    # Convert the chain ID to a bridge chain name
    chain = cast(BridgeChain, BRIDGE_CHAIN_NAMES[chain_id])

    # Get the wallet
    wallet = client.wallets.get(wallet_id)

    # Create the offramp request
    offramp_response = client.fiat.offramp.create(
        user_id=user_id,
        amount=str(amount_in_usdc),
        destination=offramp_destination,
        provider=offramp_provider,
        source=offramp_create_params.Source(
            chain=chain,
            currency="usdc",
            from_address=wallet.address,
        ),
    )

    # Send USDC to the target address
    rpc_response = send_usdc(
        client=client,
        wallet_id=wallet_id,
        recipient_address=offramp_response.deposit_instructions.to_address,
        amount_in_usdc=float(offramp_response.deposit_instructions.amount),
        chain_id=chain_id,
    )

    return rpc_response
