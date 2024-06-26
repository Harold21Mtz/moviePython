from pydantic import BaseModel, Field


class CategoryRequestDto(BaseModel):
    category_name: str = Field(min_length=5, max_length=20)
    category_description: str = Field(min_length=5, max_length=100)

    class Config:
        json_schema_extra = {
            "example": {
                "category_name": "Action",
                "category_description": "Intense, exciting and adrenaline-filled scenes."
            }
        }


class CategoryResponseDto(BaseModel):
    category_id: int
    category_name: str
    category_description: str
