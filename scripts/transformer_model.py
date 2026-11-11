"""Standalone BERT representation module from report section 5.3."""

import torch.nn as nn
from transformers import BertModel


class BERTURLClassifier(nn.Module):
    """Return the report's 64-dimensional transformed BERT representation.

    Despite the source snippet's class name, its final layer is not a binary
    classification head: it returns 64 values per input example.
    """

    def __init__(self):
        super(BERTURLClassifier, self).__init__()
        self.bert = BertModel.from_pretrained("bert-base-uncased")
        self.fc = nn.Linear(768, 128)
        self.relu = nn.ReLU()
        self.output = nn.Linear(128, 64)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        x = self.fc(outputs.pooler_output)
        x = self.relu(x)
        return self.output(x)
