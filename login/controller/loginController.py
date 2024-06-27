from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.configDatabase import get_db
from login.schema.loginDto import LoginDto
from login.loginService import LoginService

loginRouter = APIRouter()


@loginRouter.post("/", response_model=dict)
def login(login: LoginDto, login_service: LoginService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = login_service.login(session, login)
    return response
