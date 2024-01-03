from pydantic import BaseModel
from typing import List, Optional

class Response(BaseModel):
    code: int
    ok: bool
    msg: str
    error: str


class ResponseList(Response):
    data: List = []


class ResponseDictionary(Response):
    data: Optional[dict] = None
