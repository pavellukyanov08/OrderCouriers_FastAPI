from typing import List

from pydantic import BaseModel


class DistrictBase(BaseModel):
    name: str

    class Config:
        from_attributes = True
