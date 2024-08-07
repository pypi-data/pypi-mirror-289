from dataclasses import dataclass as __dataclass, field
from api.endpoints import *


@__dataclass
class Params:
    wstoken: str
    wsfunction: Endpoint
    moodlewsrestformat: str = field(default="json")
