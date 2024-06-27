from fastapi import HTTPException
from sqlalchemy.orm import Session

from user.model.user import User
from user.schema.userDto import UserRequestDto, UserResponseDto
from user.repository.userRepository import UserRepository
from middlewares.bcrypt import hash_password


class UserService:

    def create_user(self, db: Session, new_user: UserRequestDto) -> dict:
        emailExist = self.exist_email(db, new_user.email)

        usernameExist = self.exist_username(db, new_user.username)

        if emailExist:
            raise HTTPException(status_code=409, detail='Email already registered')

        if usernameExist:
            raise HTTPException(status_code=409, detail='Username already registered')

        new_user.password = hash_password(new_user.password)

        return UserRepository(db).create_user(new_user)

    def update_user(self, db: Session, user_id: int, new_user: UserRequestDto) -> dict:
        userExist = UserRepository(db).get_user(user_id)

        if not userExist:
            raise HTTPException(status_code=404, detail='User not found')

        return UserRepository(db).update_user(new_user, userExist)

    def exist_email(self, db: Session, email: str):
        return UserRepository(db).exist_user_by_email(email)

    def exist_username(self, db: Session, username: str):
        return UserRepository(db).exist_user_by_username(username)

    def get_user_by_id(self, db: Session, user_id) -> dict:
        userExist = UserRepository(db).get_user(user_id)

        if not userExist:
            raise HTTPException(status_code=404, detail='User not found')

        user_response = UserResponseDto(
            id=userExist.id,
            username=userExist.username,
            email=userExist.email
        )
        return user_response.model_dump()

    def get_all_users(self, db: Session) -> dict:
        users = UserRepository(db).get_all_users()
        users_response = []

        for user in users:
            user_response = UserResponseDto(
                id=user.id,
                username=user.username,
                email=user.email
            )
            users_response.append(user_response.model_dump())
        return {"Message": "All users", "data": users_response}

    def delete_user(self, db: Session, user_id: int) -> dict:
        userExist = UserRepository(db).get_user(user_id)

        if not userExist:
            raise HTTPException(status_code=404, detail='User not found')

        return UserRepository(db).delete_user(userExist)

    @staticmethod
    def user_exist_by_email(self, db: Session, email: str) -> User:
        user = UserRepository(db).userExist(email)
        if not user:
            raise HTTPException(status_code=401, detail="User does not exist")
        return user
