import ast
import random
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.models.prediction import Prediction
from app.database.models.user import User
from app.services.auth import AuthService
from app.database.config import get_db
from app.database.models.model import Model
from app.database.models.source_code import SourceCode
from app.database.schemas.generic_response import GenericResponse
from app.database.schemas.prediction import BugCheckRequestSchema, BugCheckType, BugPositionResponseSchema, BuggyPositionSchema
from app.services.model import ModelService
from app.services.buggy_position import BuggyPositionService
from app.services.prediction.prediction import BiLSTMPredictionService, CustomBiLSTMPredictionService, PredictionService
from app.services.source_code import SourceCodeService
from app.services.user import UserService

predictionRouter = APIRouter()
auth_service = AuthService()

@predictionRouter.post('/{source_code_id}', response_model=GenericResponse[BugPositionResponseSchema])
def predict(source_code_id: int, user: dict = Depends(auth_service.get_current_user), db: Session = Depends(get_db)):
    """API nhận source code id và trả về kết quả dự đoán dự đoán lỗi và gợi ý điều chỉnh trên mã nguồn đó."""
    try:
        source_code: SourceCode = SourceCodeService(db).get_by_id(source_code_id)
        if source_code.user_id != user['sub']:
            raise HTTPException(status_code=401, detail='Cannot access this source code.')
        model_type = ast.literal_eval(ConfigRepository(db).get_by_name('ACTIVE_MODEL').value)
        # if model_type is None or len(model_type) == 0:
        #     model_type = 'BiLSTM'
        # else:
        #     model_type = random.choice(model_type)
        # NOTE: Override model_type for testing
        model_type = 'CustomBiLSTM'
        model: Model = ModelService(db).get_model(model_type, source_code.problem_id)
        prediction = CustomBiLSTMPredictionService(db, model).create_prediction(source_code)
        return GenericResponse(data=prediction)
    except Exception as e:
        print(e)
        raise e
    
@predictionRouter.put('/bug-check', response_model=GenericResponse[List[BuggyPositionSchema]])
def bug_check(request: BugCheckRequestSchema, user: dict = Depends(auth_service.get_current_user), db: Session = Depends(get_db)):
    """API nhận các lỗi được đánh dấu và lưu thông tin này vào db."""
    try:
        prediction_service = PredictionService(db)
        prediction: Prediction = prediction_service.validate_prediction(request.prediction_id, user['sub'])
        if prediction.is_feedback_submitted is False:
            prediction_service.update(prediction.id, { 'is_feedback_submitted': True })
        if request.type == BugCheckType.TOKEN_ERROR:
            bug_list = list(BuggyPositionService(db).token_error(request.prediction_id, request.position))
        elif request.type == BugCheckType.SUGGESTION_USEFUL:
            bug_list = list(BuggyPositionService(db).suggestion_useful(request.prediction_id, request.position))
        return GenericResponse(data=bug_list)
    except Exception as e:
        print(e)
        raise e