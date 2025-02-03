from fastapi import HTTPException
from app.database.repositories.user import UserRepository


class UserService:
    def __init__(self, db):
        self.__user_repository = UserRepository(db)

    def get_user(self, user_id):
        user = self.__user_repository.get_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
        else:
            return user