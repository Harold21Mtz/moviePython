import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from fastapi import HTTPException
from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError
from login.schema.loginDto import LoginDto
from typing import Dict, Union

load_dotenv()

secretKey = os.getenv("SECRET_KEY")
token_duration_minutes = 15


def create_token(login: LoginDto) -> str:
    data = login.dict()
    expiration = datetime.now(tz=timezone.utc) + timedelta(minutes=token_duration_minutes)
    data.update({"exp": expiration})
    token: str = encode(payload=data, key=secretKey, algorithm="HS256")
    return token


def validate_token(token: str) -> Dict[str, Union[str, bool]]:
    try:
        payload = decode(token, secretKey, algorithms=["HS256"])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
