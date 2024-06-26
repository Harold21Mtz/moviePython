from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session

from config.configDatabase import get_db
from middlewares.jwt_manager import validate_token
from user.model.user import User


# class JWTBearer(HTTPBearer):
#     async def __call__(self, request: Request):
#         auth = await super().__call__(request)
#         data = validate_token(auth.credentials)
#         if data['email'] != "harold@gmail.com":
#             raise HTTPException(status_code=403, detail="Credenciales invalidas")


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        token = credentials.credentials
        payload = validate_token(token)

        user_email = payload.get("email")
        if not user_email:
            raise HTTPException(status_code=403, detail="Invalid token: email not found")

        user = db.query(User).filter(User.email == user_email).first()
        if not user:
            raise HTTPException(status_code=403, detail="User not found")
        return payload
