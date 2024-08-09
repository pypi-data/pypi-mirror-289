from typing import Any, List, Optional

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


class Instrument(BaseModel):
    currencyTitle: str
    networkTitle: str


class DepositAddress(BaseModel):
    instrument: Instrument
    depositAddress: str
    depositAddressMemo: Any


class Pair(BaseModel):
    instrumentFrom: InstrumentFrom
    instrumentTo: InstrumentTo


class OrderEvent(BaseModel):
    createdAt: str
    kind: str


class Quotes(BaseModel):
    sellQuote: Quote
    buyQuote: Quote


class ClaimedPublicRate(BaseModel):
    claimedAmountToReceive: str
    finalNetworkFeeAmount: str
    platformFee_Absolute: str
    fixedRate_maxAmount: str
    fixedRate_maxTimeMinutes: int
    fixedRate_maxRateVolatilityPercent: str
    price: str
    quotes: Quotes
    updatedAt: str


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
    liquidityProviderQuotes: Quotes
    price: str
    marketLeftPrice: str
    marketRightPrice: str
    marketAmountToGet: str
    marketAmountToGetUSDT: str
    quotesWithoutNetworkFee: Quotes
    quotes: Quotes


class CreateOrderReq(BaseModel):
    instrumentFrom: InstrumentFrom
    instrumentTo: InstrumentTo
    rateMode: str
    destinationAddress: str
    destinationAddressMemo: Optional[int] = None
    refundAddress: Optional[str] = None
    refundAddressMemo: Optional[int] = None
    claimedPublicRate: ClaimedPublicRate
    claimedNetworkFee: str
    legacyOrderId: Optional[int] = None
    referrerId: Optional[str] = None
    claimedDepositAmount: str
    browserFingerprint: str
    markup: str


class CreateOrderRes(BaseModel):
    orderId: int
    createdAt: str
    userEmail: Any
    isPlatformEmail: bool
    legacyOrderId: Any
    refundAddress: Any
    destinationAddress: str
    destinationAddressMemo: Any
    claimedNetworkFee: str
    rateMode: str
    claimedDepositAmount: str
    amountToGet: str
    pair: Pair
    orderEvents: List[OrderEvent]
    depositAddress: DepositAddress
    deposits: List
    withdrawals: List
    KYCFormLink: Any
    liquidityProviderPublicCode: str
    claimedPublicRate: ClaimedPublicRate

