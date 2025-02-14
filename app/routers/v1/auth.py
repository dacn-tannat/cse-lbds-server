from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.services.user import UserService
from app.services.auth import AuthService
from app.database.config import get_db
from app.services.auth import AuthService

authRouter = APIRouter()

@authRouter.post('/login/google')
async def login_google(data: dict, db: Session = Depends(get_db)):
    code = data["code"]
    if not code:
        raise HTTPException(status_code=400, detail='Code not provided')

    # Get user_info from Google
    user_info = AuthService().get_user_info_from_google(code)
    
    # Create new user in case 
    user_service = UserService(db)
    if user_service.get_user(user_info['sub']) is None:
        user_service.create_user(user_info)

    # Create access token for user
    access_token = AuthService().create_access_token(user_info)

    return {'access_token': access_token, 'user': user_info}