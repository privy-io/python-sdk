from typing import Any, Dict, List

from ..types.user import (
    LinkedAccount,
    LinkedAccountApple,
    LinkedAccountEmail,
    LinkedAccountPhone,
    LinkedAccountGitHub,
    LinkedAccountGoogle,
    LinkedAccountSolana,
    LinkedAccountTiktok,
    LinkedAccountDiscord,
    LinkedAccountSpotify,
    LinkedAccountTwitter,
    LinkedAccountCrossApp,
    LinkedAccountEthereum,
    LinkedAccountLinkedIn,
    LinkedAccountTelegram,
    LinkedAccountCustomJwt,
    LinkedAccountFarcaster,
    LinkedAccountInstagram,
    LinkedAccountSmartWallet,
)


def convert_to_linked_accounts(
    linked_accounts: List[Dict[str, Any]],
) -> List[LinkedAccount]:
    converted_linked_accounts: List[LinkedAccount] = []
    for account in linked_accounts:
        account_type = account["type"]
        latest_verified_at = account.get("lv")

        if account_type == "email":
            converted_linked_accounts.append(
                LinkedAccountEmail(
                    address=account["address"],
                    type="email",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "phone":
            converted_linked_accounts.append(
                LinkedAccountPhone(
                    phoneNumber=account["phone_number"],
                    type="phone",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "wallet":
            if account.get("chain_type") == "ethereum":
                converted_linked_accounts.append(
                    LinkedAccountEthereum(
                        address=account["address"],
                        chain_type="ethereum",
                        type="wallet",
                        wallet_client="unknown",
                        wallet_client_type=account.get("wallet_client_type"),
                        latest_verified_at=latest_verified_at,
                    )
                )
            elif account.get("chain_type") == "solana":
                converted_linked_accounts.append(
                    LinkedAccountSolana(
                        address=account["address"],
                        chain_type="solana",
                        type="wallet",
                        wallet_client="unknown",
                        wallet_client_type=account.get("wallet_client_type"),
                        latest_verified_at=latest_verified_at,
                    )
                )
        elif account_type == "smart_wallet":
            converted_linked_accounts.append(
                LinkedAccountSmartWallet(
                    address=account["address"],
                    smart_wallet_type=account["smart_wallet_type"],
                    type="smart_wallet",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "farcaster":
            converted_linked_accounts.append(
                LinkedAccountFarcaster(
                    fid=float(account["fid"]),
                    username=account.get("username"),
                    type="farcaster",
                    owner_address=account["oa"],
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "google_oauth":
            converted_linked_accounts.append(
                LinkedAccountGoogle(
                    subject=account["subject"],
                    email=account["email"],
                    name=account.get("name"),
                    type="google_oauth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "twitter_oauth":
            pfp = account.get("pfp")
            if pfp:
                if pfp.startswith("default"):
                    pfp = f"https://abs.twimg.com/sticky/default_profile_images/{pfp}"
                elif not pfp.startswith("https://"):
                    pfp = f"https://pbs.twimg.com/profile_images/{pfp}"

            converted_linked_accounts.append(
                LinkedAccountTwitter(
                    subject=account["subject"],
                    username=account["username"],
                    name=account.get("name"),
                    profile_picture_url=pfp,
                    type="twitter_oauth",
                    latest_verified_at=latest_verified_at,
                    verified_at=latest_verified_at,
                )
            )
        elif account_type == "discord_oauth":
            converted_linked_accounts.append(
                LinkedAccountDiscord(
                    subject=account["subject"],
                    username=account["username"],
                    type="discord_oauth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "github_oauth":
            converted_linked_accounts.append(
                LinkedAccountGitHub(
                    subject=account["subject"],
                    username=account["username"],
                    type="github_oauth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "spotify_oauth":
            converted_linked_accounts.append(
                LinkedAccountSpotify(
                    subject=account["subject"],
                    type="spotify_oauth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "instagram_oauth":
            converted_linked_accounts.append(
                LinkedAccountInstagram(
                    subject=account["subject"],
                    username=account["username"],
                    type="instagram_oauth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "tiktok_oauth":
            converted_linked_accounts.append(
                LinkedAccountTiktok(
                    subject=account["subject"],
                    username=account.get("username"),
                    type="tiktok_oauth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "linkedin_oauth":
            converted_linked_accounts.append(
                LinkedAccountLinkedIn(
                    subject=account["subject"],
                    email=account.get("email"),
                    type="linkedin_oauth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "apple_oauth":
            converted_linked_accounts.append(
                LinkedAccountApple(
                    subject=account["subject"],
                    email=account.get("email"),
                    type="apple_oauth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "cross_app":
            converted_linked_accounts.append(
                LinkedAccountCrossApp(
                    subject=account["subject"],
                    provider_app_id=account["provider_app_id"],
                    embedded_wallets=account.get("embedded_wallets", []),
                    smart_wallets=account.get("smart_wallets", []),
                    type="cross_app",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "custom_auth":
            converted_linked_accounts.append(
                LinkedAccountCustomJwt(
                    custom_user_id=account["custom_user_id"],
                    type="custom_auth",
                    latest_verified_at=latest_verified_at,
                )
            )
        elif account_type == "telegram":
            converted_linked_accounts.append(
                LinkedAccountTelegram(
                    telegram_user_id=account["telegram_user_id"],
                    username=account["username"],
                    type="telegram",
                    latest_verified_at=latest_verified_at,
                )
            )

    return converted_linked_accounts
