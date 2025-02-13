import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2AuthorizationCodeBearer
import httpx
import jwt
from datetime import datetime, timedelta
import pytz
from sqlalchemy.orm import Session

from app.database.config import get_db
from app.services.user import UserService

load_dotenv('.env')

secret_key = os.getenv("JWT_SECRET_KEY")
algorithm = os.getenv("JWT_ALGORITHM")

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://accounts.google.com/o/oauth2/auth?scope=email profile",
    tokenUrl="https://oauth2.googleapis.com/token"
)

def create_access_token(user_info: dict):
    """Tạo access_id với múi giờ Asia/Ho_Chi_Minh (GMT+7)"""
    tz = pytz.timezone("Asia/Ho_Chi_Minh")
    exp_time = datetime.now(tz) + timedelta(days=1)  # Hết hạn sau 2h

    payload = {
        "sub": user_info["sub"],  
        "email": user_info.get("email"),
        "exp": int(exp_time.timestamp())  # Chuyển thành timestamp
    }
    return jwt.encode(payload, secret_key, algorithm=algorithm)

async def verify_google_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Xác minh token với Google OAuth2 và tạo access_id"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://www.googleapis.com/oauth2/v3/userinfo",
            headers={"Authorization": f"Bearer {token}"}
        )
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_info = response.json()  # Lấy thông tin người dùng
    _userService = UserService(db) # Khởi tạo UserService
    if _userService.get_user(user_info["sub"]) is None:
        _userService.create_user(user_info)
    access_token = create_access_token(user_info)  # Tạo access_id riêng
    return {"user": user_info, "access_token": access_token}

def get_current_user(access_id: str = Security(oauth2_scheme)):
    """Giải mã access_id để lấy thông tin user"""
    try:
        payload = jwt.decode(access_id, secret_key, algorithms=[algorithm])
        return payload  # Trả về thông tin user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")