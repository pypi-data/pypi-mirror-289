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
config = Config(api_url="https://quickex.io", api_public="changeme", api_secret="changeme")
sdk = QuickexSDK(config)
```

## Get instrument

```python
res = InstrumentReq(currencyTitle="USDT", networkTitle="TRC20")
instrument = sdk.get_instrument(res)
```

## Get rate

```python
res = RateReq(
    instrumentFromCurrencyTitle="BTC",
    instrumentFromNetworkTitle="BTC",
    instrumentToCurrencyTitle="USDT",
    instrumentToNetworkTitle="TRC20",
    claimedDepositAmount="10000",
    rateMode="FLOATING",
    claimedDepositAmountCurrency="USDT",
    markup="1.0",
)
rate = sdk.get_rate(res)
```

## Create order

```python
res = RateReq(
    instrumentFromCurrencyTitle="BTC",
    instrumentFromNetworkTitle="BTC",
    instrumentToCurrencyTitle="USDT",
    instrumentToNetworkTitle="TRC20",
    claimedDepositAmount="10000",
    rateMode="FLOATING",
    claimedDepositAmountCurrency="BTC",
    markup="0.3",
)
rate = sdk.get_rate(res)
public_rate = ClaimedPublicRate(
    claimedAmountToReceive=rate.amountToGet,
    finalNetworkFeeAmount=rate.finalNetworkFeeAmount,
    platformFee_Absolute=rate.platformFee_Absolute,
    price=rate.price,
    quotes=rate.quotes,
    updatedAt=rate.updatedAt,
)
req = CreateOrderReq(
    instrumentFrom=rate.instrumentFrom,
    instrumentTo=rate.instrumentTo,
    destinationAddress='TFe5tdqSy8CMGMDVHPJHLTK8hrAL6ddUpD',
    destinationAddressMemo=None,
    refundAddress=None,
    refundAddressMemo=None,
    claimedPublicRate=public_rate,
    claimedNetworkFee=rate.finalNetworkFeeAmount,
    legacyOrderId=None,
    referrerId=None,
    claimedDepositAmount=rate.amountToGive,
    rateMode="FLOATING",
    markup=rate.markup,
)

new_order = sdk.create_order(req)
```

## License

`quickex-sdk` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
