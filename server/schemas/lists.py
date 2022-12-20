from pydantic import BaseModel, Field

class CreateListSchema(BaseModel):
    title: str = Field(...)
    uid: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Sample Title",
                "uid": "123456-1234-1234-123456"
            }
        }

class UpdateListSchema(BaseModel):
    lid: str = Field(...)
    title: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "lid": "123456-1234-1234-123456",
                "title": "Sample Title"
            }
        }