import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.config import get_db
from app.services.prediction.prediction import PredictionService
from app.services.source_code import SourceCodeService

# Load the .env file
load_dotenv('.env')

predictionRouter = APIRouter()
model_path = os.getenv("PREDICTION_MODEL_PATH")

@predictionRouter.post('/{source_code_id}')
def predict(source_code_id: int, db: Session = Depends(get_db)):
    try:
        source_code = SourceCodeService(db).get_by_id(source_code_id)
        prediction = PredictionService(model_path, 50, 157, 64, 200, 2, 0.5).predict(source_code.source_code)
        return prediction
    except Exception as e:
        print(e)
        raise e