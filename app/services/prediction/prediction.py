import torch

from app.services.prediction.encoder import CTokenEncoder
from app.services.prediction.lexer import CustomCLexer
from app.services.prediction.model import BiLSTMModel

class PredictionService:
    def __init__(self, model_path, seq_length, vocab_size, embed_size, hidden_size, num_layers, dropout):
        self.seq_length = seq_length
        self.model = BiLSTMModel(vocab_size=vocab_size, embed_size=embed_size, hidden_size=hidden_size, num_layers=num_layers, dropout=dropout)
        # self.model = DataParallel(self.model)
        # Load weight for correct model
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        self.model.eval()
    
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
        
    def predict(self, source_code):
        lexer, encoder = CustomCLexer(), CTokenEncoder()
        # Tokenize and encode src_code
        raw_tokens = lexer.tokenize(source_code)
        encoded_tokens = encoder.encode_tokens(raw_tokens)
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
            
            # Get predictions which prob is > 0.1
            top_predictions = [pred for pred in predictions if pred[2] > 0.01] #  list of (token, id, prob) but prob > 0.1
            
            output_token_prob = next((pred for pred in predictions if pred[1] == output), None)

            if output_token_prob not in top_predictions:
                incorrect_pred.append({
                    'position': i,
                    'correct_probability': output_token_prob[2],
                    'original_token': output_token_prob,
                    'predicted_tokens': predictions[0]
                })

        sorted_incorrect_pred = sorted(incorrect_pred, key=lambda x: x['correct_probability'])
        top_10_incorrect = sorted_incorrect_pred[:10]
        sorted_top_10_incorrect = sorted(top_10_incorrect, key=lambda x: x['position'])
        result = []
        for i, incorrect in enumerate(sorted_top_10_incorrect):
            result.append({
                'id': i,
                'position': incorrect['position'],
                'original_token': incorrect['original_token'][0],
                'predicted_token': incorrect['predicted_tokens'][0]
            })
        return result