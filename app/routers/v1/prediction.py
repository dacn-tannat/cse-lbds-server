import ast
import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.config import get_db
from app.database.models.buggy_position import BuggyPosition
from app.database.repositories.config import ConfigRepository
from app.database.schemas.prediction import BugCheckRequestSchema, BugCheckResponseSchema
from app.services.model import ModelService
from app.services.prediction.buggy_position import BuggyPositionService
from app.services.prediction.prediction import BiLSTMPredictionService
from app.services.source_code import SourceCodeService

predictionRouter = APIRouter()

@predictionRouter.post('/{source_code_id}', response_model=BugCheckResponseSchema)
def predict(source_code_id: int, db: Session = Depends(get_db)):
    """API nhận source code id và trả về kết quả dự đoán dự đoán lỗi và gợi ý điều chỉnh trên mã nguồn đó."""
    try:
        source_code = SourceCodeService(db).get_by_id(source_code_id)
        model_type = ast.literal_eval(ConfigRepository(db).get_by_name('ACTIVE_MODEL').value)
        if model_type is None or len(model_type) == 0:
            model_type = 'BiLSTM'
        else:
            model_type = random.choice(model_type)
        model = ModelService(db).get_model(model_type, source_code.problem_id)
        return BiLSTMPredictionService(db, model).create_prediction(source_code)
    except Exception as e:
        print(e)
        raise e
    
@predictionRouter.put('/bug-check')
def bug_check(request: BugCheckRequestSchema, db: Session = Depends(get_db)):
    """API nhận các lỗi được đánh dấu và lưu thông tin này vào db."""
    try:
        return BuggyPositionService(db).bug_check(request.prediction_id, request.position)
    except Exception as e:
        print(e)
        raise e