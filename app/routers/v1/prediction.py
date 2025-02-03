import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.config import get_db
from app.database.models.prediction import Prediction
from app.database.repositories.prediction import PredictionRepository
from app.database.repositories.user import UserRepository
from app.services.model import ModelService
from app.services.prediction.prediction import PredictionService
from app.services.source_code import SourceCodeService
from app.services.user import UserService

predictionRouter = APIRouter()

@predictionRouter.post('/{source_code_id}')
def predict(source_code_id: int, db: Session = Depends(get_db)):
    try:
        user_id = 0
        source_code = SourceCodeService(db).get_by_id(source_code_id)
        user = UserService(db).get_user(user_id)
        model = ModelService(db).get_model(user.model_type, source_code.problem_id)
        return PredictionService(db, model).create_prediction(source_code)
    except Exception as e:
        print(e)
        raise e