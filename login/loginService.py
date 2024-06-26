from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from login.loginDto import LoginDto
from login.loginRepository import LoginRepository
from middlewares.jwt_manager import create_token


class LoginService:
    def login(self, db: Session, login: LoginDto) -> dict:
        user = LoginRepository(db).userExist(login.email)
        userValid = LoginRepository(db).login(login)
        if not user:
            raise HTTPException(status_code=401, detail="User does not exist")
        if user.password != login.password:
            raise HTTPException(status_code=401, detail="Email or password is incorrect")

        return {"token": create_token(login)}
        # return jsonable_encoder({"user": userValid})
