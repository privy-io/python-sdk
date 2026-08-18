# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PolicyMethod"]

PolicyMethod: TypeAlias = Literal[
    "eth_sendTransaction",
    "eth_signTransaction",
    "eth_signUserOperation",
    "eth_signTypedData_v4",
    "personal_sign",
    "eth_sign7702Authorization",
    "wallet_sendCalls",
    "signTransaction",
    "signAndSendTransaction",
    "signMessage",
    "exportPrivateKey",
    "exportSeedPhrase",
    "signTransactionBytes",
    "signRawMessageBytes",
    "tron_sendTransaction",
    "tron_signTransaction",
    "xrpl_signTransaction",
    "earn_deposit",
    "earn_withdraw",
    "transfer",
    "*",
]
