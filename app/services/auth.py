from fastapi import HTTPException
import pytz
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv
import httpx

load_dotenv('.env')

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')

class AuthService:
    def __init__(self):
        pass

    async def get_user_info_from_google(self, code: str):
        """Lấy access token từ Google và lấy thông tin user"""
        # Get access token from Google by FE code
        async with httpx.AsyncClient() as client:
            token_response = await client.post(
                'https://oauth2.googleapis.com/token',
                data={
                    'client_id': cls.GOOGLE_CLIENT_ID,
                    'client_secret': cls.GOOGLE_CLIENT_SECRET,
                    'code': code,
                    'grant_type': "authorization_code",
                    'redirect_uri': cls.GOOGLE_REDIRECT_URI
                },
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )

        if token_response.status_code != 200:
            raise HTTPException(status_code=400, detail='Failed to exchange code for token')

        google_access_token = token_response.json().get('access_token')

        # Get user_info by Google access_token
        async with httpx.AsyncClient() as client:
            user_response = await client.get(
                'https://www.googleapis.com/oauth2/v3/userinfo',
                headers={'Authorization': f'Bearer {google_access_token}'}
            )

        if user_response.status_code != 200:
            raise HTTPException(status_code=400, detail='Failed to fetch user info')

        return user_response.json()
    
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