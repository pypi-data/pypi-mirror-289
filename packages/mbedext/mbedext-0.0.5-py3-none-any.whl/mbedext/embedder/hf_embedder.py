from typing import Union, Optional

import torch
from transformers import AutoTokenizer

from .embedder import Embedder


class HFEmbedder(Embedder):
    def __init__(self, model, text, *args, **kwargs) -> None:
        super().__init__(model, text)

    def embed(self, batch: Union[list[str], str]):
        tokenizer = AutoTokenizer.from_pretrained(self.model.name_or_path)
        tokenize_batch = tokenizer(batch, return_tensors='pt', padding="max_length", truncation=True)

        with torch.no_grad():
            outputs = self.model(**tokenize_batch)
            return outputs.last_hidden_state.mean(dim=1)

