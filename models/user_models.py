from pydantic import BaseModel
from typing import List

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    balance: int
    lista: List[str]
