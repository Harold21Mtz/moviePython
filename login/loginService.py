from fastapi import HTTPException
from sqlalchemy.orm import Session

from login.schema.loginDto import LoginDto
from middlewares.jwt_manager import create_token
from middlewares.bcrypt import verify_password
from user.service.userService import UserService


class LoginService:
    def login(self, db: Session, login: LoginDto) -> dict:
        user = UserService.user_exist_by_email(self, db, login.email)
        if not verify_password(login.password, user.password):
            raise HTTPException(status_code=401, detail="Email or password is incorrect")

        return {"token": create_token(login)}
        # return jsonable_encoder({"user": userValid})
