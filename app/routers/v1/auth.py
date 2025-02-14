from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.services.user import UserService
from app.services.auth import AuthService
from app.database.config import get_db
import httpx
from dotenv import load_dotenv
import os

authRouter = APIRouter()

load_dotenv('.env')

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI')

@authRouter.post('/login/google')
async def login_google(data: dict, db: Session = Depends(get_db)):
    code = data["code"]
    if not code:
        raise HTTPException(status_code=400, detail='Code not provided')

    # Get access_token from Google
    async with httpx.AsyncClient() as client:
        token_response = await client.post(
            'https://oauth2.googleapis.com/token',
            data={
                'client_id': GOOGLE_CLIENT_ID,
                'client_secret': GOOGLE_CLIENT_SECRET,
                'code': code,
                'grant_type': "authorization_code",
                'redirect_uri': GOOGLE_REDIRECT_URI
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )

    if token_response.status_code != 200:
        raise HTTPException(status_code=400, detail='Failed to exchange code for token')
    
    token_data = token_response.json()
    google_access_token = token_data.get('access_token')
    
    # use Google access token to get user information
    async with httpx.AsyncClient() as client:
        user_response = await client.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            headers={'Authorization': f'Bearer {google_access_token}'}
        )
    if user_response.status_code != 200:
        raise HTTPException(status_code=400, detail='Failed to fetch user info')

    user_info = user_response.json()
    
    # Create new user in case 
    user_service = UserService(db)
    if user_service.get_user(user_info['sub']) is None:
        user_service.create_user(user_info)

    # Create access token for user
    access_token = AuthService().create_access_token(user_info)

    return {'access_token': access_token, 'user': user_info}