import os
import dotenv
from dataclasses import dataclass


@dataclass
class Config:
    url: str
    api_token: str


def setup():
    dotenv.load_dotenv()
    url = os.getenv("URL")
    api_token = os.getenv("API_TOKEN")
    return Config(f"{url}/webservice/rest/server.php", api_token)
