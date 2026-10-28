## Setting up the environment

### With `uv`

We use [uv](https://docs.astral.sh/uv/) to manage dependencies because it will automatically provision a Python environment with the expected Python version. To set it up, run:

```sh
$ ./scripts/bootstrap
```

Or [install uv manually](https://docs.astral.sh/uv/getting-started/installation/) and run:

```sh
$ uv sync --all-extras
```

You can then run scripts using `uv run python script.py` or by manually activating the virtual environment:

```sh
# manually activate - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate

# now you can omit the `uv run` prefix
$ python script.py
```

### Without `uv`

Alternatively if you don't want to install `uv`, you can stick with the standard `pip` setup by ensuring you have the Python version specified in `.python-version`, create a virtual environment however you desire and then install dependencies using this command:

```sh
$ pip install -r requirements-dev.lock
```

## Modifying/Adding code

Most of the SDK is generated code. Modifications to code will be persisted between generations, but may
result in merge conflicts between manual patches and changes from the generator. The generator will never
modify the contents of the `src/privy/lib/` and `examples/` directories.

## Adding and running examples

All files in the `examples/` directory are not modified by the generator and can be freely edited or added to.

```py
# add an example to examples/<your-example>.py

#!/usr/bin/env -S uv run python
…
```

```sh
$ chmod +x examples/<your-example>.py
# run the example against your api
$ ./examples/<your-example>.py
```

## Using the repository from source

If you’d like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```sh
$ pip install git+ssh://git@github.com/privy-io/python-sdk.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, all you have to do is run this command:

```sh
$ uv build
# or
$ python -m build
```

Then to install:

```sh
$ pip install ./path-to-wheel-file.whl
```

## Running tests

```sh
$ ./scripts/test
```

### Live integration tests

Integration tests make real requests to the Privy staging API; they do not use mocks. Copy `.env.example` to
`.env`, populate `TEST_APP_ID`, `TEST_APP_SECRET`, and `JWT_AUTH_SK`, export the values, and run:

```sh
$ set -a
$ source .env
$ set +a
$ uv run pytest -m integration tests/integration
```

Each integration test must create the resources it needs rather than depending on pre-existing wallets, users, or
other API resources. `TEST_API_URL` may be used to override the staging URL, but the suite refuses to target the
production API.

## Linting and formatting

This repository uses [ruff](https://github.com/astral-sh/ruff) and
[black](https://github.com/psf/black) to format the code in the repository.

To lint:

```sh
$ ./scripts/lint
```

To format and fix all ruff issues automatically:

```sh
$ ./scripts/format
```

## Publishing and releases

Development happens on `main` in the private `privy-io/python-sdk-private` repo. The public
[`privy-io/python-sdk`](https://github.com/privy-io/python-sdk) repo is updated only when a
release is published, so its `main` matches the latest release. Releases are managed by
[release-please](https://github.com/googleapis/release-please); see
[RELEASING.md](./RELEASING.md) for how to cut a release.

If a release doesn't publish through this pipeline, you may want to publish it manually.

### Publish with a GitHub workflow

You can release to package managers by using [the `Publish PyPI` GitHub action](https://www.github.com/privy-io/python-sdk/actions/workflows/publish-pypi.yml). This requires a setup organization or repository secret to be set up.

### Publish manually

If you need to manually release a package, you can run the `bin/publish-pypi` script with a `PYPI_TOKEN` set on
the environment.

### Contributing from the public repo

You can open pull requests against `main` in `privy-io/python-sdk`, but they aren't merged
there. A maintainer re-lands the change in the private repo with you as co-author and closes
your PR. The change ships in the next release. The failing `Public PR` check on your PR is
that reminder, not a problem with your change.

### Importing a public pull request (maintainers)

From a clone of `python-sdk-private`, with `N` set to the public PR number:

```sh
git fetch origin main
git fetch https://github.com/privy-io/python-sdk.git "pull/$N/head:public-pr-$N"
git switch -c "import/python-sdk-$N" origin/main
git diff "$(git merge-base origin/main "public-pr-$N")" "public-pr-$N" | git apply -3
```

`git apply -3` stages the change and leaves conflict markers where it can't apply cleanly.
Resolve them, then commit with the public PR's title and credit the author
(`git log -1 --format='%an <%ae>' "public-pr-$N"`):

```sh
git commit -m "<public PR title>" \
  -m "Imported from privy-io/python-sdk#$N" \
  -m "Co-authored-by: <author name> <author email>"
git push -u origin HEAD
```

Open a PR in `python-sdk-private` with the same `Imported from` and `Co-authored-by` lines in
the body, so they survive a squash merge. Then close the public PR with a comment that the
change was imported and will ship in the next release.
