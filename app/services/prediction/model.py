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