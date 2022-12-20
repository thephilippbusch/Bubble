from pydantic import BaseModel, Field

class CreateEntrySchema(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    lid: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Sample Name",
                "description": "Sample Description",
                "lid": "123456-1234-1234-123456"
            }
        }

class UpdateEntrySchema(BaseModel):
    eid: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "eid": "123456-1234-1234-123456",
                "name": "Sample Title",
                "description": "Sample Description"
            }
        }