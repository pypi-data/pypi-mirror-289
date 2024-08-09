from typing import Union, Optional

import torch
from transformers import AutoTokenizer

from .embedder import Embedder


class HFEmbedder(Embedder):
    def __init__(self, model, text, *args, **kwargs) -> None:
        super().__init__(model, text)
        self.model = self.model.to(self.dev)

    def embed(self, batch: Union[list[str], str], *args, pooling_method: Optional[Union[str, int]], **kwargs):
        tokenizer = AutoTokenizer.from_pretrained(self.model.name_or_path)
        tokenize_batch = tokenizer(batch, return_tensors='pt', padding="max_length", truncation=True).to(self.dev)

        with torch.no_grad():
            outputs = self.model(**tokenize_batch)
            if isinstance(pooling_method, int):
                return outputs.last_hidden_state[:, pooling_method, :]
            elif isinstance(pooling_method, str):
                if pooling_method == "mean":
                    return outputs.last_hidden_state.mean(dim=1)
            else:
                raise ValueError(f"Unkown pooling method: {pooling_method}")

