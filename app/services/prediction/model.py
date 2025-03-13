import torch
import torch.nn as nn

class BiLSTMModel(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size, num_layers, dropout):
        super(BiLSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers, batch_first=True,
                            dropout=dropout,
                            bidirectional=True)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_size * 2, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        
        # He Initialization for hidden state
        h0 = torch.randn(self.lstm.num_layers * 2, x.size(0), self.lstm.hidden_size, device=x.device) * torch.sqrt(torch.tensor(2.0) / self.lstm.hidden_size)
        c0 = torch.randn(self.lstm.num_layers * 2, x.size(0), self.lstm.hidden_size, device=x.device) * torch.sqrt(torch.tensor(2.0) / self.lstm.hidden_size)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])  # Get the last hidden state
        return out

class CustomBiLSTMModel(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size, num_layers, dropout,
                # New hyperparameters
                score_range,        # score range from 0 - 10 (11 distinct value)        
                embed_score_size    # should be equal to embed_size
                ):
        super(CustomBiLSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size + embed_score_size,
                            hidden_size, 
                            num_layers, 
                            batch_first=True,
                            dropout=dropout,
                            bidirectional=True)
        # Previous version: self.fc = nn.Linear(hidden_size * 2, vocab_size)
        self.fc_token = nn.Linear(self.lstm.hidden_size, vocab_size)
        self.fc_score = nn.Linear(self.lstm.hidden_size, score_range)

    def forward(self, x, scores):
        x = self.embedding(x)
    
        # Create score vector
        scores = scores.unsqueeze(-1).repeat(1, 1, 64)
        # Attach score into embedding layer
        x = torch.cat([x, scores], dim=-1)
        
        # He Initialization for hidden state
        h0 = torch.randn(self.lstm.num_layers * 2, x.size(0), self.lstm.hidden_size, device=x.device) * torch.sqrt(torch.tensor(2.0) / self.lstm.hidden_size)
        c0 = torch.randn(self.lstm.num_layers * 2, x.size(0), self.lstm.hidden_size, device=x.device) * torch.sqrt(torch.tensor(2.0) / self.lstm.hidden_size)

        out, _ = self.lstm(x, (h0, c0))
        # Split output from hidden state into 2 parts: token and score
        out_token = self.fc_token(out[:, -1, :self.lstm.hidden_size])
        out_score = self.fc_score(out[:, -1, self.lstm.hidden_size:])

        return out_token, out_score