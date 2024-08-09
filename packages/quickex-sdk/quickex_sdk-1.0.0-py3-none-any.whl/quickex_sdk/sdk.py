from pydantic_core import from_json

from src.quickex_sdk.client import Client
from src.quickex_sdk.models import Config, InstrumentReq, InstrumentRes, RateRes, RateReq

HTTP_TIMEOUT_SECONDS = 10


class QuickexSDK:
    def __init__(self, config: Config):
        self.client = Client(config)

    def get_instrument(self, body: InstrumentReq):
        r = self.client.post('/api/v2/instruments/public/one', body.model_dump_json())
        if r.status_code in [200, 201]:
            # instrument_dict = json.loads(r.json())
            return InstrumentRes.model_validate_json(r.text)
        else:
            responce = r.json()
            raise Exception(responce.message + str(r.status_code))

    def get_rate(self, body: RateReq) -> RateRes:
        r = self.client.post('/api/v2/rates/public/one', body.model_dump_json())
        if r.status_code in [200, 201]:
            # instrument_dict = json.loads(r.json())
            return RateRes.model_validate_json(r.text)
        else:
            responce = r.json()
            raise Exception(responce.message + str(r.status_code))
