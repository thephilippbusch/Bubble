from pydantic import BaseModel, Field

class UserSignSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "max_mustermann",
                "password": "1234XYZ"
            }
        }