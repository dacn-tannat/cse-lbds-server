from typing import List
from fastapi import HTTPException
import torch

from app.database.models.buggy_position import BuggyPosition
from app.database.models.model import Model
from app.database.models.prediction import Prediction
from app.database.models.source_code import SourceCode
from app.database.repositories.buggy_position import BuggyPositionRepository
from app.database.repositories.prediction import PredictionRepository
from app.database.schemas.prediction import BugPositionResponseSchema, BuggyPositionSchema
from app.services.prediction.encoder import CTokenEncoder
from app.services.prediction.lexer import CustomCLexer
from app.services.prediction.model import BiLSTMModel
from app.services.source_code import SourceCodeService

class BiLSTMPredictionService:
    def __init__(self, db, model: Model):
        self.model_config = model
        self.seq_length = model.hyperparameter['seq_length']
        self.model = BiLSTMModel(vocab_size=model.hyperparameter['vocab_size'], embed_size=model.hyperparameter['embed_size'], hidden_size=model.hyperparameter['hidden_size'], num_layers=model.hyperparameter['num_layers'], dropout=model.hyperparameter['dropout'])
        # self.model = DataParallel(self.model)
        # Load weight for correct model
        self.model.load_state_dict(torch.load(model.model_path, map_location=torch.device('cpu')))
        self.model.eval()
        self.__prediction_repository = PredictionRepository(db)
        self.__buggy_position_repository = BuggyPositionRepository(db)
    
    def predict_all_tokens(self, input_seq):
        '''
        Generate ra xác suất cho tất cả token và trả về list (token_value, probability)
        List trả về được sort theo prob giảm dần
        '''
        input_tensor = torch.tensor(input_seq, dtype=torch.long).unsqueeze(0)

        with torch.no_grad(): # not calculate gradient
            output = self.model(input_tensor)
            probabilities = torch.softmax(output, dim=1).squeeze(0)

        token_prob_pairs = [(token, prob.item()) for token, prob in enumerate(probabilities)]
        token_prob_pairs.sort(key=lambda x: x[1], reverse=True)

        return token_prob_pairs

    def generate_sequences(self, input, seq_length):
        '''
        Generate ra các inputs (sequences) và outputs tương ứng cho 1 source code
        '''
        inputs = []
        targets = []
        for i in range(len(input) - seq_length):
            inputs.append(input[i:i+seq_length])
            targets.append(input[i+seq_length])
        return inputs, targets
        
    def predict(self, source_code) -> List[BuggyPositionSchema]:
        lexer, encoder = CustomCLexer(), CTokenEncoder()
        # Tokenize and encode src_code
        raw_tokens = lexer.tokenize(source_code)
        encoded_tokens, encoded_tokens_with_index = encoder.encode_tokens(raw_tokens)
        id_to_token = encoder.get_vocab_id_to_token() # map from id -> token
        
        padded_encoded_tokens = [0] * self.seq_length + encoded_tokens # Padding
        # Create inputs and outputs
        inputs, outputs = self.generate_sequences(padded_encoded_tokens, self.seq_length)
        incorrect_pred = []
        for i, (input, output) in enumerate(zip(inputs, outputs)):
            # Get probability for all tokens in vocab
            predictions = self.predict_all_tokens(input)
            predictions = [
                (id_to_token.get(pred[0], pred[0]), pred[0], pred[1])
                for pred in predictions
            ] # list of (token, id, prob)
              
            output_token_prob = next((pred for pred in predictions if pred[1] == output), None)

            if output_token_prob is not None and output_token_prob[2] < 0.1:
                incorrect_pred.append({
                    'position': i,
                    'start_index': encoded_tokens_with_index[i][1],
                    'correct_probability': output_token_prob[2],
                    'original_token': output_token_prob,
                    'predicted_tokens': predictions[0]
                })

        sorted_incorrect_pred = sorted(incorrect_pred, key=lambda x: x['correct_probability'])
        top_10_incorrect = sorted_incorrect_pred[:10]
        sorted_top_10_incorrect = sorted(top_10_incorrect, key=lambda x: x['position'])
        result = []
        for i, incorrect in enumerate(sorted_top_10_incorrect):
            result.append(BuggyPositionSchema(
                id=i,
                position=incorrect['position'],
                start_index=incorrect['start_index'],
                original_token=incorrect['original_token'][0],
                predicted_token=incorrect['predicted_tokens'][0],
                is_used=False
            ))
        return result
    
    def create_prediction(self, source_code: SourceCode) -> BugPositionResponseSchema:
        buggy_position = self.predict(source_code.source_code)
        prediction = self.__prediction_repository.create(Prediction(
            model_id=self.model_config.id,
            source_code_id=source_code.id
        ))

        for pos in buggy_position:
            pos_dict = pos.model_dump()  # Chuyển Pydantic Model thành dictionary
            pos_dict["prediction_id"] = prediction.id  # Thêm field mới
            self.__buggy_position_repository.create(BuggyPosition(**pos_dict))  # Chuyển thành BuggyPosition


        return BugPositionResponseSchema(
            id=prediction.id,
            model_id=prediction.model_id,
            source_code_id=prediction.source_code_id,
            buggy_position=buggy_position
        )
    
class PredictionService:
    def __init__(self, db):
        self.db = db
        self.__prediction_repository = PredictionRepository(db)

    def get_by_id(self, id) -> Prediction:
        prediction = self.__prediction_repository.get_by_id(id)
        if prediction is None:
            raise HTTPException(status_code=404, detail='Prediction not found')
        return prediction
    
    def validate_prediction(self, prediction_id, user_id) -> bool:
        prediction = self.get_by_id(prediction_id)
        source_code = SourceCodeService(self.db).get_by_id(prediction.source_code_id)
        if source_code.user_id != user_id:
            raise HTTPException(status_code=401, detail='Cannot access this source code.')
        
        return True