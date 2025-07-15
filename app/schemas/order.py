from pydantic import BaseModel


class OrderBase(BaseModel):
    name: str

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    name: str
    district: str


class OrderResponse(BaseModel):
    name: str
    courier: int
    status: int
    district: int

    class Config:
        from_attributes = True


class OrderCreateResponse(BaseModel):
    id: int
    courier_id: int
    status: int
    district: int

    model_config = {
        'from_attributes': True,
    }