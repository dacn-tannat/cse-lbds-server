from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_id(self, id):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, entity):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, entity):
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, id):
        entity = self.get_by_id(id)
        self.db.delete(entity)
        self.db.commit()
        return entity