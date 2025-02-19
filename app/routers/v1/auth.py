from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.schemas.generic_response import GenericResponse
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

    auth_service = AuthService()
    user_service = UserService(db)
    
    # Get user_info from Google
    user_info = await auth_service.get_user_info_from_google(code)
        
    # Create new user in case 
    if user_service.get_user(user_info['sub']) is None:
        user_service.create_user(user_info)

    # Create access token for user
    access_token = auth_service.create_access_token(user_info)

    return GenericResponse(data={'access_token': access_token, 'user': user_info})
