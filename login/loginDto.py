from pydantic import BaseModel, EmailStr, Field


class LoginDto(BaseModel):
    email: EmailStr
    password: str = Field(min_length=5, max_length=15)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "harold@gmail.com",
                "password": "Holaa"
            }
        }
