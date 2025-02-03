from fastapi import HTTPException
from app.database.repositories.model import ModelRepository


class ModelService:
    def __init__(self, db):
        self.__model_repository = ModelRepository(db)

    def get_model(self, model_type, problem_id):
        model = self.__model_repository.get_by_type_and_problem(model_type, problem_id)
        if model is None:
            raise HTTPException(status_code=404, detail='Model not found')
        return model