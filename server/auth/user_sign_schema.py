from pydantic import BaseModel, Field

class UserSignInSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "max_mustermann",
                "password": "1234XYZ"
            }
        }

class UserSignUpSchema(BaseModel):
    username: str = Field(...)
    name: str = Field(...)
    surname: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "max_mustermann",
                "name": "Mustermann",
                "surname": "Max",
                "password": "1234XYZ"
            }
        }