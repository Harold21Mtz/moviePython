from login.loginDto import LoginDto
from user.model.user import User


class LoginRepository:
    def __init__(self, db):
        self.db = db

    def userExist(self, email):
        return self.db.query(User).filter(User.email == email).first()

    def login(self, login: LoginDto):
        return self.db.query(User).filter(User.email == login.email, User.password == login.password).first()
