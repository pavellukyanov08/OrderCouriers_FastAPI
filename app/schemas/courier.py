from pydantic import BaseModel


class CourierBase(BaseModel):
    name: str
    districts: list[str]


class CourierCreate(CourierBase):
    pass


class CourierResponse(BaseModel):
    id: int
    name: str
    districts: list[str]


    class Config:
        from_attributes=True

