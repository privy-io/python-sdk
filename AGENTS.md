# Python SDK

Python SDK (`privy-client`) for the Privy API. Stainless-generated core with a hand-authored `PrivyClient` and service layer composed on top.

## Commands

```sh
./scripts/bootstrap                            # install Python and dependencies with uv
./scripts/format                               # Ruff formatting and safe fixes
./scripts/lint                                 # Ruff, Pyright, mypy, import check
./scripts/test                                 # offline tests across Python/Pydantic versions
./scripts/test tests/test_authorization.py     # focused offline test
uv run pytest -m integration tests/integration # live staging tests; requires exported .env values
```

Run `./scripts/format`, `./scripts/lint`, and the smallest relevant test set before finishing. The full test script intentionally excludes integration tests.

## Directory Structure

```
src/privy/_client.py                 # GENERATED sync and async API clients
src/privy/resources/ types/          # GENERATED resources, params, and response models
src/privy/_*.py                     # GENERATED transport and support code
src/privy/lib/client.py              # CUSTOM synchronous PrivyClient
src/privy/lib/                       # CUSTOM services, signing, JWT exchange, request helpers
tests/api_resources/                 # generated-resource request tests
tests/test_*.py                      # offline custom/unit tests
tests/integration/                   # live staging tests
.env                                 # gitignored staging credentials when created locally
```

## Key Patterns

### Put new behavior under `src/privy/lib/`—avoid editing generated files

Stainless regenerates most of `src/privy/`. Generated files contain:

```python
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
```

The generator never modifies `src/privy/lib/`, so custom client, authorization, and service behavior belongs there.

DO add custom behavior to the preserved layer:

```python
# src/privy/lib/wallets.py
class PrivyWalletsService(WalletsResource):
    def __init__(self, client: PrivyAPI, jwt_exchanger: JWTExchangeService | None = None) -> None:
        super().__init__(client)
        self._jwt_exchanger = jwt_exchanger
```

DON'T add it directly to a generated resource:

```python
# src/privy/resources/wallets/wallets.py — GENERATED
def update(...):
    ...
```

Generated edits may persist temporarily but can conflict on regeneration and leave public behavior outside the intended extension layer.

### Custom services extend or compose generated resources

`src/privy/lib/client.py` constructs the public synchronous `PrivyClient` and exposes `Privy*Service` instances. Resource-shaped services subclass generated resources and delegate request execution to `super()`. Chain helpers such as `PrivyEthereumService`, `PrivySolanaService`, and `PrivyTronService` compose `PrivyWalletsService`.

DO preserve the public naming and delegation pattern:

```python
class PrivyPoliciesService(PoliciesResource):
    def __init__(self, client: PrivyAPI, request_expiry_provider: RequestExpiryProvider) -> None:
        super().__init__(client)
        self._request_expiry_provider = request_expiry_provider
```

DON'T recreate generated URLs, serialization, retries, or response parsing when the generated method can perform the request.

### Do not assume async parity in the custom layer

The generated `PrivyAPI` and `AsyncPrivyAPI` have matching generated APIs, but the hand-authored `PrivyClient` and its authorization-aware services are synchronous. Async custom behavior requires an explicit design covering JWT exchange, caching, signing, request options, and tests.

### Prepare authorized mutations through shared helpers

Use `PrivyRequestOptions`, `AuthorizationContext`, `prepare_request`, `build_request_url`, and the existing JWT exchange/request-expiry helpers. They keep canonicalization, authorization signatures, user-JWT exchange, idempotency keys, and request expiry consistent.

```python
prepared = prepare_request(
    app_id=self._client.app_id,
    method="PATCH",
    url=build_request_url(self._client, path),
    body=body,
    authorization_context=options.authorization_context,
    jwt_exchanger=self._jwt_exchanger,
)
```

Do not canonicalize payloads, sign them, or assemble authorization headers independently inside each service.

### Keep generated method inputs intact

Copy mutable request dictionaries before removing wrapper-only fields. Preserve generated parameter names and use `cast` where necessary to satisfy strict Pyright and mypy checks. A custom wrapper should add headers or options without changing generated response types.

### Separate offline and live tests

Offline tests use pytest and must not require credentials. Live tests are marked `integration`, live under `tests/integration/`, and use the staging-only client from `conftest.py`. The fixture refuses the production API URL.

For wallet and chain behavior, reuse `tests/integration/wallet_setup.py`:

- `setup_test_wallet_resources()` creates fresh users, key pairs, and a quorum.
- `create_test_wallets()` creates ownerless, key-owned, user-owned, and quorum-owned wallets.
- `WALLET_CASES` defines the ownership matrix.

Create the resources each integration test needs instead of relying on pre-existing state. Export `TEST_APP_ID`, `TEST_APP_SECRET`, and `JWT_AUTH_SK` before running live tests. Never target production.

## Pull Requests

Use a Conventional Commit title. Keep generated API updates separate from handwritten service changes when possible.
