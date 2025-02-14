from fastapi import HTTPException
import pytz
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv

load_dotenv('.env')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')

class AuthService:
    def __init__(self):
        pass

    def create_access_token(self, user_info: dict):
        """Tạo access_id với múi giờ Asia/Ho_Chi_Minh (GMT+7)"""
        tz = pytz.timezone("Asia/Ho_Chi_Minh")
        exp_time = datetime.now(tz) + timedelta(days=1)  # Hết hạn sau 24h

        payload = {
            "sub": user_info["sub"],
            "email": user_info.get("email"),
            "exp": int(exp_time.timestamp())
        }
        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    def get_current_user(access_id: str):
        """Giải mã access_id để lấy thông tin user"""
        try:
            payload = jwt.decode(access_id, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            return payload  # Trả về thông tin user
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")