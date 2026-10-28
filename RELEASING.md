# Releasing

Releases are cut by [release-please](https://github.com/googleapis/release-please) in the
private `privy-io/python-sdk-private` repo, then promoted to the public
[`privy-io/python-sdk`](https://github.com/privy-io/python-sdk) repo, which publishes to PyPI.
Tags are `vX.Y.Z`.

Public `main` only moves when a release is promoted, so it always matches the latest stable
release.

## Stable releases (from `main`)

1. 👤 Merge changes into `main` in `python-sdk-private`.
2. 🤖 On every push to `main`, release-please opens or updates the release PR (`release: X.Y.Z`)
   in `python-sdk-private`.
3. 👤 Approve and merge the release PR.
4. 🤖 CI runs the [release workflow](./.github/workflows/release-please.yml), which tags
   `vX.Y.Z` and creates the GitHub Release in `python-sdk-private`.
5. 🤖 The release triggers the [promote workflow](./.github/workflows/stlc-promote.yml), which:
   - fast-forwards `main` in `python-sdk` to the tag commit;
   - pushes the tag to `python-sdk`;
   - creates the matching GitHub Release in `python-sdk`, which triggers the
     [publish PyPI workflow](./.github/workflows/publish-pypi.yml) there.
6. 👤 Update the changelog in [our public docs](https://docs.privy.io).

The public release notes link to `python-sdk` commits and leave out PR numbers, since those
refer to private PRs.
