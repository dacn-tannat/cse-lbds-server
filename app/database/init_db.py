from app.database.config import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)
