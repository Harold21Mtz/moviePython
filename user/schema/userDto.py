from pydantic import BaseModel, Field, EmailStr


class UserRequestDto(BaseModel):
    username: str = Field(min_length=4, max_length=64)
    email: EmailStr
    password: str = Field(min_length=4, max_length=64)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "haroldmartinez",
                "email": "harold@gmail.com",
                "password": "Harold"
            }
        }


class UserResponseDto(BaseModel):
    id: int
    username: str
    email: EmailStr
