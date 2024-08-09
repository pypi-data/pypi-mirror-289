from typing import Optional

from pydantic import BaseModel, ConfigDict


class Config(BaseModel):
    api_url: str
    api_public: str
    api_secret: str


class InstrumentReq(BaseModel):
    currencyTitle: str
    networkTitle: str


class InstrumentRes(BaseModel):
    model_config = ConfigDict(strict=True)

    currencyTitle: str
    networkTitle: str
    okexCurrencyFriendlyTitle: str
    precisionDecimals: int
    requiresMemo: bool
    currencyLogoLink: str


class ValidateAddressReq(BaseModel):
    currencyTitle: str
    networkTitle: str
    address: str


class RateReq(BaseModel):
    instrumentFromCurrencyTitle: str
    instrumentFromNetworkTitle: str
    instrumentToCurrencyTitle: str
    instrumentToNetworkTitle: str
    claimedDepositAmount: str
    rateMode: str
    claimedDepositAmountCurrency: str
    markup: str


class InstrumentFrom(BaseModel):
    currencyTitle: str
    networkTitle: str
    precisionDecimals: int


class InstrumentTo(BaseModel):
    currencyTitle: str
    networkTitle: str
    precisionDecimals: int


class DepositRules(BaseModel):
    minAmount: str
    maxAmount: str


class WithdrawalFeeRules(BaseModel):
    maxAmount: str
    minAmount: str


class WithdrawalRules(BaseModel):
    minAmount: str
    maxAmount: str
    withdrawalFeeRules: WithdrawalFeeRules


class Quote(BaseModel):
    baseValue: str
    quoteValue: str


class LiquidityProviderQuotes(BaseModel):
    sellQuote: Quote
    buyQuote: Quote


class QuotesWithoutNetworkFee(BaseModel):
    sellQuote: Quote
    buyQuote: Quote


class RateRes(BaseModel):
    instrumentFrom: InstrumentFrom
    instrumentTo: InstrumentTo
    depositRules: DepositRules
    withdrawalRules: WithdrawalRules
    minConfirmationsToWithdraw: int
    minConfirmationsToTrade: int
    updatedAt: str
    liquidityProviderPublicCode: str
    amountToGet: str
    amountToGetUSDT: str
    amountToGive: str
    marketMinAmount: str
    enableFixedRate: bool
    amountToGiveCurrencyTitle: str
    rateMode: str
    finalNetworkFeeAmount: str
    platformFee_Absolute: Optional[str] = None
    liquidityProviderQuotes: LiquidityProviderQuotes
    price: str
    marketLeftPrice: str
    marketRightPrice: str
    marketAmountToGet: str
    marketAmountToGetUSDT: str
    quotesWithoutNetworkFee: QuotesWithoutNetworkFee