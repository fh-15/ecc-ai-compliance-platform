from pydantic import BaseModel


class ECCControlResponse(BaseModel):
    id: int
    domain: str
    control_code: str
    title: str
    description: str

    class Config:
        from_attributes = True
