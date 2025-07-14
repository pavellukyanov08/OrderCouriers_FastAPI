from pydantic import BaseModel


class DistrictBase(BaseModel):
    id: int
    name: str

    model_config = {
        'from_attributes': True
    }
