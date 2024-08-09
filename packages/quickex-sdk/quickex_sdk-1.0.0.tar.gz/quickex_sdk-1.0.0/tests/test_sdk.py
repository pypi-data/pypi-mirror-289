from src.quickex_sdk.models import Config, InstrumentReq, RateReq
from src.quickex_sdk.sdk import QuickexSDK

api_url_base = 'https://qa.cointocoin.io'
api_public_base = 'cmWnXEiUeD10uMgz1x3h0hy22EzhtqgpOzgdOHc0J5Y='
api_secret_base = 'ed83154e6916cb9ccbbfa6fbdc1776447a306546d00d459917a33a67496b2f10'

def test_sdk_class():
    config = Config(api_url=api_url_base, api_public=api_public_base, api_secret=api_secret_base)
    sdk = QuickexSDK(config)
    assert sdk.client.api_url == config.api_url
    assert sdk.client.api_public == config.api_public
    assert sdk.client.api_secret == config.api_secret


def test_sdk_get_instrument_class():
    config = Config(api_url=api_url_base, api_public=api_public_base, api_secret=api_secret_base)
    sdk = QuickexSDK(config)
    assert sdk.client.api_url == config.api_url
    assert sdk.client.api_public == config.api_public
    assert sdk.client.api_secret == config.api_secret
    res = InstrumentReq(currencyTitle="USDT", networkTitle="TRC20")
    instrument = sdk.get_instrument(res)

    assert instrument.currencyTitle == res.currencyTitle
    assert instrument.networkTitle == res.networkTitle


def test_sdk_get_instrument_fail_class():
    config = Config(api_url=api_url_base, api_public=api_public_base, api_secret=api_secret_base)
    sdk = QuickexSDK(config)
    assert sdk.client.api_url == config.api_url
    assert sdk.client.api_public == config.api_public
    assert sdk.client.api_secret == config.api_secret

    try:
        sdk.get_instrument(InstrumentReq(currencyTitle="test", networkTitle="test"))
        assert False
    except Exception:
        assert True


def test_sdk_get_rate_class():
    config = Config(api_url=api_url_base, api_public=api_public_base, api_secret=api_secret_base)
    sdk = QuickexSDK(config)
    assert sdk.client.api_url == config.api_url
    assert sdk.client.api_public == config.api_public
    assert sdk.client.api_secret == config.api_secret
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

    assert rate.instrumentFrom.currencyTitle == res.instrumentFromCurrencyTitle
    assert rate.instrumentFrom.networkTitle == res.instrumentFromNetworkTitle
    assert rate.instrumentTo.currencyTitle == res.instrumentToCurrencyTitle
    assert rate.instrumentTo.networkTitle == res.instrumentToNetworkTitle
    assert rate.amountToGive == res.claimedDepositAmount


def test_sdk_get_rate_fail_class():
    config = Config(api_url=api_url_base, api_public=api_public_base, api_secret=api_secret_base)
    sdk = QuickexSDK(config)
    assert sdk.client.api_url == config.api_url
    assert sdk.client.api_public == config.api_public
    assert sdk.client.api_secret == config.api_secret
    res = RateReq(
        instrumentFromCurrencyTitle="BTC1",
        instrumentFromNetworkTitle="BTC",
        instrumentToCurrencyTitle="USDT",
        instrumentToNetworkTitle="TRC20",
        claimedDepositAmount="10000",
        rateMode="FLOATING",
        claimedDepositAmountCurrency="USDT",
        markup="1.0",
    )
    try:
        sdk.get_rate(res)
        assert False
    except Exception:
        assert True