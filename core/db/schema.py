from pydantic import BaseModel
from datetime import datetime


class UserSchema(BaseModel):
    user_id: int
    name: str
    reg_date: str
    up_date: str
