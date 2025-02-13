from app.database.models.user import User
from app.database.repositories.user import UserRepository


class UserService:
    def __init__(self, db):
        self.__user_repository = UserRepository(db)

    def get_user(self, user_id):
        return self.__user_repository.get_by_id(user_id)
        
    def create_user(self, user):
        return self.__user_repository.create(User(
            id = user.get("sub"),
            email = user.get("email"),
            name = user.get("name"),
            picture = user.get("picture")
        ))