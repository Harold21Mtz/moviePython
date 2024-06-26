from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from config.configDatabase import get_db
from sqlalchemy.orm import Session

from user.schema.userDto import UserRequestDto
from user.service.userService import UserService

userRouter = APIRouter()


@userRouter.get("/all", response_model=dict)
def get_all_users(user_service: UserService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = user_service.get_all_users(session)
    return response


@userRouter.get("/{user_id}", response_model=dict)
def get_user_by_id(user_id: int, user_service: UserService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = user_service.get_user_by_id(session, user_id)
    return response


@userRouter.post("/", response_model=dict)
def register_user(new_user: UserRequestDto, user_service: UserService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = user_service.create_user(session, new_user)
    return response


@userRouter.put("/{user_id}", response_model=dict)
def update_user(user_id: int, update_user: UserRequestDto, user_service: UserService = Depends(),
                session: Session = Depends(get_db)) -> dict:
    response = user_service.update_user(session, user_id, update_user)
    return response


@userRouter.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, user_service: UserService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = user_service.delete_user(session, user_id)
    return response

