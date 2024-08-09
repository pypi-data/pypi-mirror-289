# Quickex SDK

[![PyPI - Version](https://img.shields.io/pypi/v/йquickex-sdk.svg)](https://pypi.org/project/йquickex-sdk)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/йquickex-sdk.svg)](https://pypi.org/project/йquickex-sdk)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install quickex-sdk
```
## Usage

```python
config = Config(api_url=api_url_base, api_public=api_public_base, api_secret=api_secret_base)
sdk = QuickexSDK(config)
```

## Get instrument

```python
res = InstrumentReq(currencyTitle="USDT", networkTitle="TRC20")
instrument = sdk.get_instrument(res)
```

## License

`quickex-sdk` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
