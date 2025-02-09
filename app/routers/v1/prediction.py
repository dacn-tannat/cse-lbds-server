from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.config import get_db
from app.database.schemas.prediction import BugCheckRequestSchema
from app.services.model import ModelService
from app.services.prediction.buggy_position import BuggyPositionService
from app.services.prediction.prediction import ModelPredictionService
from app.services.source_code import SourceCodeService
from app.services.user import UserService

predictionRouter = APIRouter()

@predictionRouter.post('/{source_code_id}')
def predict(source_code_id: int, db: Session = Depends(get_db)):
    """API nhận source code id và trả về kết quả dự đoán dự đoán lỗi và gợi ý điều chỉnh trên mã nguồn đó."""
    try:
        user_id = 0
        source_code = SourceCodeService(db).get_by_id(source_code_id)
        user = UserService(db).get_user(user_id)
        model = ModelService(db).get_model(user.model_type, source_code.problem_id)
        return ModelPredictionService(db, model).create_prediction(source_code)
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