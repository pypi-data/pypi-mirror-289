from abc import ABC, abstractmethod


class Embedder(ABC):
    def __init__(self, model, text) -> None:
        self.model = model
        self.text = text

    @abstractmethod
    def embed(self, batch):
        raise NotImplementedError