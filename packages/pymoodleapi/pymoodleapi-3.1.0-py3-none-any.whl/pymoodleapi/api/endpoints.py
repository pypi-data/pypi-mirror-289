from dataclasses import dataclass as __dataclass
from requests import get
from typing import Callable
import pymoodleapi.api.api_response_objects as response_object


@__dataclass
class Endpoint:
    return_object: type
    request_type: Callable
    function_name: str


@__dataclass
class GetAllCourses(Endpoint):
    return_object: list[response_object.Course]
    request_type: Callable = get
    function_name: str = "core_course_get_courses"
