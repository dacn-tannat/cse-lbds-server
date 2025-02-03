from app.database.repositories.base import BaseRepository
from app.database.models.source_code import SourceCode
from sqlalchemy.orm import Session

class SourceCodeRepository(BaseRepository):
    def __init__(self, db: Session, model = SourceCode):
        super().__init__(db, model)