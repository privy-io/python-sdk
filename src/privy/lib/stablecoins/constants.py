from typing import Dict

# Bridge chain name to EIP-155 chain ID mapping
BRIDGE_CHAIN_IDS: Dict[str, int] = {
    "ethereum": 1,
    "base": 8453,
    "arbitrum": 42161,
    "polygon": 137,
    "optimism": 10,
}

# USDC contract addresses by chain ID
USDC_CONTRACT_ADDRESSES: Dict[int, str] = {
    1: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # Ethereum Mainnet
    8453: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",  # Base
    42161: "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",  # Arbitrum
    137: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",  # Polygon
    10: "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",  # Optimism
}

# Reverse mapping (EIP-155 chain ID to bridge chain name)
BRIDGE_CHAIN_NAMES: Dict[int, str] = {id: name for name, id in BRIDGE_CHAIN_IDS.items()}
