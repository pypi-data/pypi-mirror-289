from pydantic_core import from_json

from src.quickex_sdk.client import Client
from src.quickex_sdk.models import Config, InstrumentReq, InstrumentRes, RateRes, RateReq, CreateOrderReq, \
    CreateOrderRes


class QuickexSDK:
    def __init__(self, config: Config):
        self.client = Client(config)

    def get_instrument(self, body: InstrumentReq):
        r = self.client.post('/api/v2/instruments/public/one', body.model_dump_json())
        if r.status_code in [200, 201]:
            return InstrumentRes.model_validate_json(r.text)
        else:
            response = r.json()
            raise Exception(response.message + str(r.status_code))

    def get_rate(self, body: RateReq) -> RateRes:
        r = self.client.post('/api/v2/rates/public/one', body.model_dump_json())
        if r.status_code in [200, 201]:
            return RateRes.model_validate_json(r.text)
        else:
            response = r.json()
            raise Exception(response.message + str(r.status_code))

    def get_create_order(self, body: CreateOrderReq) -> CreateOrderRes:
        r = self.client.post('/api/v2/orders/public/create', body.model_dump_json())
        if r.status_code in [200, 201]:
            return CreateOrderRes.model_validate_json(r.text)
        else:
            response = r.json()
            raise Exception(response.message + str(r.status_code))
