from pymoodleapi.settings import setup, Config
from pymoodleapi.api.api import Params
from pymoodleapi.api.endpoints import Endpoint
from pymoodleapi.api.api_response_objects import ResponseObject
from dataclasses import asdict


#
# lbibbb
class Client:
    __config: Config
    url: str
    token: str

    def __init__(self):
        self.__config = setup()
        self.url = self.__config.url
        self.token = self.__config.api_token

    def call(self, endpoint: Endpoint) -> ResponseObject:
        response: endpoint.return_object = endpoint.request_type(
            self.url,
            params=asdict(
                Params(wstoken=self.token, wsfunction=endpoint.function_name)
            ),
        ).json()
        return response
