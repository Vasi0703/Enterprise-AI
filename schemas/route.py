from typing import Literal

from pydantic import BaseModel


class RouteResponse(BaseModel):

    route: Literal[
        "hr",
        "math",
        "chat"
    ]