from pydantic import BaseModel


class DataInput(BaseModel):
    data: str
