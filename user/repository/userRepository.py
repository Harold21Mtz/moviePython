from starlette import status

from login.schema.loginDto import LoginDto
from user.model.user import User
from user.schema.userDto import UserRequestDto


class UserRepository:

    def __init__(self, db):
        self.db = db

    def create_user(self, new_user: UserRequestDto):
        new_user_instance = User(**new_user.model_dump())
        self.db.add(new_user_instance)
        self.db.commit()
        return {"Message": "User created", "status_code": status.HTTP_201_CREATED}

    def get_user(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all_users(self):
        return self.db.query(User).all()

    def exist_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def exist_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def update_user(self, update_user: UserRequestDto, user: User):
        user.username = update_user.username
        user.email = update_user.email
        user.password = update_user.password
        self.db.commit()
        return {"Message": "User updated", "status_code": status.HTTP_200_OK}

    def delete_user(self, user: User):
        self.db.delete(user)
        self.db.commit()
        return {"Message": "User deleted", "status_code": status.HTTP_200_OK}

    def userExist(self, email):
        return self.db.query(User).filter(User.email == email).first()

    def login(self, login: LoginDto):
        return self.db.query(User).filter(User.email == login.email, User.password == login.password).first()
