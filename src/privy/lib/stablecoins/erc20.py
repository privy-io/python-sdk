import json

from web3 import Web3
from eth_typing import ChecksumAddress

from .constants import USDC_CONTRACT_ADDRESSES


def build_usdc_transfer_data(recipient_address: str, amount_usdc: float, chain_id: int) -> str:
    """Build the USDC transfer data for the transaction.

    Args:
        recipient_address: The address to send USDC to
        amount_usdc: The amount of USDC to send
        chain_id: The chain ID to send USDC on

    Returns:
        str: The encoded function call data for the USDC transfer
    """
    # Get the USDC contract address for the specified chain
    usdc_address = USDC_CONTRACT_ADDRESSES[chain_id]

    # USDC has 6 decimals
    amount_wei = int(amount_usdc * 10**6)

    # Create Web3 instance
    w3 = Web3()

    # Create contract instance with just the transfer function ABI
    usdc_abi = json.loads("""
    [
        {
            "inputs": [
                {"name": "to", "type": "address"},
                {"name": "amount", "type": "uint256"}
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]
    """)

    # Convert addresses to checksum format
    usdc_address_checksum: ChecksumAddress = w3.to_checksum_address(usdc_address)
    recipient_address_checksum: ChecksumAddress = w3.to_checksum_address(recipient_address)

    # Create contract instance
    contract = w3.eth.contract(address=usdc_address_checksum, abi=usdc_abi)

    # Encode the transfer function call
    return str(contract.encode_abi(abi_element_identifier="transfer", args=[recipient_address_checksum, amount_wei]))
