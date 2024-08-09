from abc import ABC, abstractmethod
from typing import Optional

import torch


class Embedder(ABC):
    def __init__(self, model, text, dev = None) -> None:
        self.model = model
        self.text = text
        self.dev = self.set_device(dev)

    @abstractmethod
    def embed(self, batch):
        raise NotImplementedError

    @staticmethod
    def set_device(dev: Optional[str] = None):
        if dev is not None:
            return torch.device(dev)
        if torch.backends.mps.is_available():
            return torch.device("mps")
        elif torch.cuda.is_available():
            return torch.device("cuda")
        else:
            return torch.device("cpu")