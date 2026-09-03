# Changelog

## 0.6.0 (2026-05-22)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/privy-io/python-sdk/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([71f0c2a](https://github.com/privy-io/python-sdk/commit/71f0c2a05914a01ab5f47dfb1fd517fd256a181a))
* **api:** api update ([b3063fa](https://github.com/privy-io/python-sdk/commit/b3063fa8ed8db0d9a91eb7e6063ab97850d9a4f4))
* **api:** api update ([8d97242](https://github.com/privy-io/python-sdk/commit/8d9724250da5ab0509dfd89dd462b8e9e28cd07b))
* **api:** api update ([bf9a256](https://github.com/privy-io/python-sdk/commit/bf9a256e9c4b838a05716ae263c7f02c24178a84))
* **api:** api update ([5a023ab](https://github.com/privy-io/python-sdk/commit/5a023ab0c686407fbff91cadb0771c920ea3265f))
* **api:** api update ([a8ca531](https://github.com/privy-io/python-sdk/commit/a8ca531e575fec59542edcdae5e972eb26c8956a))
* **api:** api update ([e824180](https://github.com/privy-io/python-sdk/commit/e824180cb6c15c42649347e3cfe5d08a64dc5819))
* **api:** api update ([f5ca7f4](https://github.com/privy-io/python-sdk/commit/f5ca7f44ef9dcf48032264033b516451cfc4c884))
* **api:** api update ([44f7389](https://github.com/privy-io/python-sdk/commit/44f738981aaec8764150ffaa53055fb44805f22b))
* **api:** api update ([b2c5bb6](https://github.com/privy-io/python-sdk/commit/b2c5bb65be72a12535b3de1a72fffae0ed14e9be))
* **api:** api update ([52ee186](https://github.com/privy-io/python-sdk/commit/52ee1863f2a7c60ecd334d22a3a7f629f7b74500))
* **api:** api update ([f0e0263](https://github.com/privy-io/python-sdk/commit/f0e0263d1c8ac00251248fbb5e4bdbb300f33f7f))
* **api:** api update ([58cd64e](https://github.com/privy-io/python-sdk/commit/58cd64e62b647e7e7365c2d642d4b32454238615))
* **api:** api update ([cf5c21c](https://github.com/privy-io/python-sdk/commit/cf5c21c8ca71fb7fecc57fdb3e112d3a0538466f))
* **api:** api update ([13bf677](https://github.com/privy-io/python-sdk/commit/13bf6775282dcbea7956dcba07ad647bdeb7fe0d))
* **api:** api update ([5a5fa1e](https://github.com/privy-io/python-sdk/commit/5a5fa1eec6456af27baa2adfde2b65cbb1be9840))
* **api:** api update ([0fc89cf](https://github.com/privy-io/python-sdk/commit/0fc89cf520e95be0e34514d2d60ebd94a7fe538f))
* **api:** api update ([837137f](https://github.com/privy-io/python-sdk/commit/837137fb6276dacc405fc2f81034b0e8d7f0d164))
* **client:** add follow_redirects request option ([0159605](https://github.com/privy-io/python-sdk/commit/015960581bd299df2667bf53e22f3e39a0c105c3))
* **client:** add support for aiohttp ([daff2b6](https://github.com/privy-io/python-sdk/commit/daff2b65a3f33e77b876aa2fc4e68f46e0d814f3))


### Bug Fixes

* **ci:** correct conditional ([6e55755](https://github.com/privy-io/python-sdk/commit/6e557559ac8dd77f3898f0bf5442901ef4c21249))
* **ci:** release-doctor — report correct token name ([ce2d602](https://github.com/privy-io/python-sdk/commit/ce2d6028f8fd2c1c11b7c35bca29a1e97478086f))
* **client:** correctly parse binary response | stream ([32f0453](https://github.com/privy-io/python-sdk/commit/32f0453dda644c57c65cd475d4cc26a4b40ff9fa))
* **client:** handle .copy() with endpoint specific URLs ([4571554](https://github.com/privy-io/python-sdk/commit/457155428c86b8ad68c5813e8756e9847ba12b89))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([79ed889](https://github.com/privy-io/python-sdk/commit/79ed889ee3b3408a7769eeb1fea3a88632d3ccdd))


### Chores

* **ci:** enable for pull requests ([c13c426](https://github.com/privy-io/python-sdk/commit/c13c42683937c154336fdaa65beb452af3ce4a67))
* **ci:** only run for pushes and fork pull requests ([401e545](https://github.com/privy-io/python-sdk/commit/401e54591a896f6ab6381d57bf61959715c36d8e))
* **docs:** remove reference to rye shell ([fadc37e](https://github.com/privy-io/python-sdk/commit/fadc37ea759680ef5412d0af125b9f2717beba21))
* **internal:** update conftest.py ([de6f87d](https://github.com/privy-io/python-sdk/commit/de6f87d57b91284b4fde1f2767ccbcf2746332ad))
* mark package as unmaintained ([#31](https://github.com/privy-io/python-sdk/issues/31)) ([128b4c1](https://github.com/privy-io/python-sdk/commit/128b4c1bdb8585c9d3a8f5d511bcd91c08ed0c34))
* **readme:** update badges ([6ed462e](https://github.com/privy-io/python-sdk/commit/6ed462e381b6f61f489c84cb1b03148d072d8e7f))
* **tests:** add tests for httpx client instantiation & proxies ([63667e2](https://github.com/privy-io/python-sdk/commit/63667e278208893cf21964210331f536c7b94aad))
* **tests:** run tests in parallel ([0afea95](https://github.com/privy-io/python-sdk/commit/0afea95ba790923350f0e78fa611f2b8901643cd))
* **tests:** skip some failing tests on the latest python versions ([5b39137](https://github.com/privy-io/python-sdk/commit/5b391375c07261ca558906e9b97fec13f81d7130))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([331350d](https://github.com/privy-io/python-sdk/commit/331350d77c2dc9f5891483a397572c39b23986c7))

## 0.5.0 (2025-06-02)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/privy-io/python-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([0a68bec](https://github.com/privy-io/python-sdk/commit/0a68becc7c4e91572ba4aa1d1f466ead87caad64))
* **api:** api update ([f79d885](https://github.com/privy-io/python-sdk/commit/f79d88592a40a77b174f9e2b3f29a70bef064b8e))
* **api:** api update ([d0a34a9](https://github.com/privy-io/python-sdk/commit/d0a34a9ca645885aff77102e3b3a8a689f9c55cc))
* **api:** api update ([311cfac](https://github.com/privy-io/python-sdk/commit/311cfac03e96773498591027b2a5699e9600bd95))
* **api:** api update ([6525a91](https://github.com/privy-io/python-sdk/commit/6525a9146936f47d6ea0c7e089ae65c28914017d))
* **users:** get user by id token ([#29](https://github.com/privy-io/python-sdk/issues/29)) ([0748598](https://github.com/privy-io/python-sdk/commit/07485989adb712e6fbdb5252b95d80653ccc0605))
* **users:** verify_access_token ([#28](https://github.com/privy-io/python-sdk/issues/28)) ([36f6b60](https://github.com/privy-io/python-sdk/commit/36f6b608bbf55368e2fd88dc803d6eccdc9ffc7f))

## 0.4.0 (2025-05-23)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/privy-io/python-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([c07dc81](https://github.com/privy-io/python-sdk/commit/c07dc81020c2bdd6144628d2fe61a57ba5854fa9))
* **api:** api update ([9c34ba7](https://github.com/privy-io/python-sdk/commit/9c34ba748ec87cec09e6f0905697d9dde553e76c))
* **api:** api update ([07f4211](https://github.com/privy-io/python-sdk/commit/07f4211ac7c5587bc4b022bbe02c64b43f8da03b))
* **api:** api update ([aaf0184](https://github.com/privy-io/python-sdk/commit/aaf01842c3476615eab8449bc4860377ce6746d6))
* **api:** api update ([02d59e6](https://github.com/privy-io/python-sdk/commit/02d59e6f8dcd396dbbb36f64697fb87b33fa8324))
* **api:** api update ([42b0cf9](https://github.com/privy-io/python-sdk/commit/42b0cf90907c7ec5a6206ebee7377d0c92c7c22c))
* **client:** add support for endpoint-specific base URLs ([0f8555b](https://github.com/privy-io/python-sdk/commit/0f8555ba919894cb10ac37956c43b5c9106a8a36))


### Bug Fixes

* **client:** endpoints with base URL with multiple environments ([de6d01a](https://github.com/privy-io/python-sdk/commit/de6d01a32b4acab6cb6e89aa0e28ce731dadc684))
* **withdraw_usdc_to_bank:** use provider's actual deposit instruction amount ([0738b97](https://github.com/privy-io/python-sdk/commit/0738b97ce9e5214f5edebf50cde2eb6f8daf4b8d))


### Chores

* **ci:** fix installation instructions ([1245a3c](https://github.com/privy-io/python-sdk/commit/1245a3c467abe7a7c32b0549547a1180c092aee3))
* **ci:** upload sdks to package manager ([cb162dd](https://github.com/privy-io/python-sdk/commit/cb162dd879f9026c56270af738a68335fb3fd4bd))
* **docs:** grammar improvements ([00d58e1](https://github.com/privy-io/python-sdk/commit/00d58e15180eb51679f712e6d12bb1a14c3877e9))
* **internal:** codegen related update ([3cc52f8](https://github.com/privy-io/python-sdk/commit/3cc52f82aa6e53a0b8d6116db76846d04ffbeec0))
* **internal:** codegen related update ([3a10681](https://github.com/privy-io/python-sdk/commit/3a10681d91d187b06e619baa3ec000bd7f36d3ff))
* **internal:** version bump ([41fbe00](https://github.com/privy-io/python-sdk/commit/41fbe0054e77966b09165bb21b4aa4606cf5890f))

## 0.3.0 (2025-05-13)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/privy-io/python-sdk/compare/v0.2.0...v0.3.0)

### Features

* **api:** add client.users.get_by_wallet_address ([faad375](https://github.com/privy-io/python-sdk/commit/faad3757b0df75250ff7ede345e094a3bba9eeee))
* **api:** api update ([48d20e5](https://github.com/privy-io/python-sdk/commit/48d20e55e0bf03abed9e236c134b21e961e252dc))
* **api:** api update ([51acddf](https://github.com/privy-io/python-sdk/commit/51acddfce5a1b356e8e67d9691ccddded62a8587))


### Bug Fixes

* **api:** add helper functions to ease onramp and offramp operations ([2a2cbfb](https://github.com/privy-io/python-sdk/commit/2a2cbfbe8cd064df52b1b5ab35126ab1e0e99faf))
* **api:** move helper functions to stablecoins package in privy.lib ([44ca3e4](https://github.com/privy-io/python-sdk/commit/44ca3e437f786571aac9aba0653df3f6a6be4fa8))


### Chores

* **internal:** version bump ([7662c16](https://github.com/privy-io/python-sdk/commit/7662c169213df1e4969e55e1ba85f571d7616052))

## 0.2.0 (2025-05-12)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/privy-io/python-sdk/compare/v0.1.0...v0.2.0)

### Features

* **api:** add fiat.get_kyc_link method ([9870254](https://github.com/privy-io/python-sdk/commit/9870254bb82a915de6910e0294914380d930a700))
* **api:** api update ([b4cfe68](https://github.com/privy-io/python-sdk/commit/b4cfe68f0664fc715e45e44a91f05f644e18a40d))
* **api:** api update ([caf67d0](https://github.com/privy-io/python-sdk/commit/caf67d047a2ac2203db1d0a6436c4ba99040e8a7))
* **api:** api update ([54d3598](https://github.com/privy-io/python-sdk/commit/54d35987e78f78f8965b02d446d3d4f198a32ac8))


### Chores

* **internal:** version bump ([1174260](https://github.com/privy-io/python-sdk/commit/1174260a8091a4b2d843c8162aa805cc2d0daa76))

## 0.1.0 (2025-05-11)

Full Changelog: [v0.1.0-alpha.8...v0.1.0](https://github.com/privy-io/python-sdk/compare/v0.1.0-alpha.8...v0.1.0)

### Features

* **api:** add fiat.get_status for /v1/users/{user_id}/fiat/status endpoint ([e1c1589](https://github.com/privy-io/python-sdk/commit/e1c15895fa2f134f1d97ec5ac0c8fee46a46eb3f))


### Documentation

* remove a few "APIs" ([#20](https://github.com/privy-io/python-sdk/issues/20)) ([583159c](https://github.com/privy-io/python-sdk/commit/583159c0157c31ce9c0337267a876908c8283aa9))

## 0.1.0-alpha.8 (2025-05-11)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/privy-io/python-sdk/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** api update ([098e618](https://github.com/privy-io/python-sdk/commit/098e6184ccfa0e89d1fd4f6c58a78d22fe709bbc))
* clean up wallet creation and user signers endpoints ([#19](https://github.com/privy-io/python-sdk/issues/19)) ([3f023ad](https://github.com/privy-io/python-sdk/commit/3f023ada6313401bb0434d20b2499cd39994c731))


### Bug Fixes

* custom user imports and formatting ([7f47551](https://github.com/privy-io/python-sdk/commit/7f475516d811bf7fc4e755faabbab00fbb81c467))
* wire up custom users resource ([bd1c718](https://github.com/privy-io/python-sdk/commit/bd1c7185b9970837cbaffb2c279966c102fb0ef1))

## 0.1.0-alpha.7 (2025-05-11)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/privy-io/python-sdk/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** add get_by_email_address and get_by_jwt_subject_id for users ([3c6327f](https://github.com/privy-io/python-sdk/commit/3c6327f4db24f2d10b910399662a4bab8d63bafa))
* **api:** api update ([4d1f19f](https://github.com/privy-io/python-sdk/commit/4d1f19f5586d7ea6d34b0eb1dc02f9111c646c07))
* **api:** api update ([d6eb8be](https://github.com/privy-io/python-sdk/commit/d6eb8be374614de095a9874a8fddb6d1462e2823))


### Bug Fixes

* **api:** add custom wallets resource ([74d382a](https://github.com/privy-io/python-sdk/commit/74d382a3369cc30144603325417bd38e3f4b4e56))
* **api:** add encryption and decryption logic for user signer endpoints ([583dbef](https://github.com/privy-io/python-sdk/commit/583dbef5973a0313c3173123d2701f65ef5f961e))
* **api:** add encryption and decryption logic for user signer endpoints ([f15edab](https://github.com/privy-io/python-sdk/commit/f15edabfc105a060103ad11aa3bd8544dba14a25))
* **api:** adjust privy wallet interfaces to be the same ([af3c0fa](https://github.com/privy-io/python-sdk/commit/af3c0fa1903e8c705670cca1764197dd6c80d150))
* **api:** simplify user signer authenticate with safe_authenticate_with_jwt method ([f2d5461](https://github.com/privy-io/python-sdk/commit/f2d5461551c2f76753a0dc365279ba5ae14c5cad))
* **api:** support custom privy wallet interfaces on PrivyAPI client ([c113573](https://github.com/privy-io/python-sdk/commit/c11357398abc4326396318edc118e7a99e5e8aa8))
* **package:** support direct resource imports ([4222919](https://github.com/privy-io/python-sdk/commit/4222919a4d1bfcddb5050f7c5f585d04d5a11b94))

## 0.1.0-alpha.6 (2025-05-09)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/privy-io/python-sdk/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** manual updates ([57406b6](https://github.com/privy-io/python-sdk/commit/57406b624d6ef566b6f13a7a0e8ffb0a95242657))


### Bug Fixes

* **api:** manually trigger build ([782a0b7](https://github.com/privy-io/python-sdk/commit/782a0b7221f45d167fbdc82f40dd7df0a9b5dad9))

## 0.1.0-alpha.5 (2025-05-09)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/privy-io/python-sdk/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** manual updates ([83d46a5](https://github.com/privy-io/python-sdk/commit/83d46a5beb437206e050c65bc57ea9950ad30ac8))

## 0.1.0-alpha.4 (2025-05-09)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/privy-io/python-sdk/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** add configure_app method on fiat resource ([1bf85de](https://github.com/privy-io/python-sdk/commit/1bf85deaadda376fa74a6d75feb7079c65d65bb8))
* **api:** api update ([41e929e](https://github.com/privy-io/python-sdk/commit/41e929e49b901782fdaea9e45f806216a58f4b57))


### Chores

* update SDK settings ([a7a26ac](https://github.com/privy-io/python-sdk/commit/a7a26ac0e2dfc9456c014b362c66d37ae6fe5edc))

## 0.1.0-alpha.3 (2025-05-09)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/privy-io/python-sdk/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** rename package name to 'privy' ([07f256e](https://github.com/privy-io/python-sdk/commit/07f256e93d320c54aa1f8f24aa68a6f4452baf8b))

## 0.1.0-alpha.2 (2025-05-09)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/privy-io/python-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update package names ([3bffca4](https://github.com/privy-io/python-sdk/commit/3bffca498362a213cbf5324174af5954cf27a53e))

## 0.1.0-alpha.1 (2025-05-09)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/privy-io/python-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** add new fiat endpoints, python package name change, and mintlify code gen ([4a4c2ce](https://github.com/privy-io/python-sdk/commit/4a4c2ce8ee8d372f6fe559742d2f561ee67766ce))
* **api:** api update ([c291977](https://github.com/privy-io/python-sdk/commit/c291977587090a1c2c8b1c12138cfde4b95f84ab))
* **api:** api update ([c05eebd](https://github.com/privy-io/python-sdk/commit/c05eebd31c80bfc90931a12a0755fc8cb871e128))
* **api:** api update ([0cf5f9f](https://github.com/privy-io/python-sdk/commit/0cf5f9f2bc005bc2c8aa16710cef9c965e8856a4))
* **api:** api update ([db04323](https://github.com/privy-io/python-sdk/commit/db04323760627cc7a57888e06a6b4d92ae1794dc))
* **api:** api update ([bbdbf44](https://github.com/privy-io/python-sdk/commit/bbdbf44af8c2919c2c30cb9e25ea03045f00b91e))
* **api:** api update ([a364e98](https://github.com/privy-io/python-sdk/commit/a364e9890dc0a24416fa534be2b2f8d92ac80f35))
* **api:** api update ([30d3023](https://github.com/privy-io/python-sdk/commit/30d3023be7d49b985f66fb10dfc8ebe2cdcf6c3e))


### Bug Fixes

* **api:** manual updates ([cd9d49c](https://github.com/privy-io/python-sdk/commit/cd9d49cc8795791a110b801433d3866f52cca401))
* correctly mark body_wallet_id as optional ([f4e9a90](https://github.com/privy-io/python-sdk/commit/f4e9a90b80c5a5b276f8361650de5d6979740f24))


### Chores

* configure new SDK language ([16981d6](https://github.com/privy-io/python-sdk/commit/16981d64e1565255f61208765dcec9588b0c790e))
* **internal:** avoid errors for isinstance checks on proxies ([599de03](https://github.com/privy-io/python-sdk/commit/599de031ffb06e3977ce8d2596d19946eab30929))
* **internal:** codegen related update ([f9c4341](https://github.com/privy-io/python-sdk/commit/f9c4341e8d13e88de3cc1c8ea366cd791f023842))
* update SDK settings ([25dfe4f](https://github.com/privy-io/python-sdk/commit/25dfe4f762db5b2cd36d2c922c06bfb92ea65f01))
