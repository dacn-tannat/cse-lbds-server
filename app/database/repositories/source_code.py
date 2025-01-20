from app.database.repositories.base import BaseRepository
from app.database.models.source_code import SourceCode
from sqlalchemy.orm import Session
from typing import List

class SourceCodeRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_id(self, id: int) -> SourceCode:
        return self.db.query(SourceCode).filter(SourceCode.id == id).first()

    def get_all(self) -> List[SourceCode]:
        return self.db.query(SourceCode).all()

    def create(self, source_code: str, ) -> SourceCode:
        source_code = SourceCode(source_code=source_code)
        self.db.add(source_code)
        self.db.commit()
        self.db.refresh(source_code)
        return source_code

    def update(self, id: int, source_code: str) -> SourceCode:
        source_code = self.get_by_id(id)
        source_code.source_code = source_code
        self.db.commit()
        self.db.refresh(source_code)
        return source_code

    def delete(self, id: int) -> SourceCode:
        source_code = self.get_by_id(id)
        self.db.delete(source_code)
        self.db.commit()
        return source_code