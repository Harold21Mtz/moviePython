from pydantic import BaseModel, Field
from datetime import datetime


class MovieRequestDto(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    overview: str = Field(min_length=3, max_length=50)
    year: str = Field(ge=2000, le=datetime.now().year)
    rating: float = Field(ge=1, le=10)
    category_id: int = Field(ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Title of a movie",
                "overview": "Description of a movie",
                "year": datetime.now().year,
                "rating": 5,
                "category_id": 1,
            }
        }


class MovieResponseDto(BaseModel):
    movie_id: int
    title: str
    overview: str
    year: str
    rating: float
    category_id: int
    category_name: str
