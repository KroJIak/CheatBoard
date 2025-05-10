
from abc import ABC, abstractmethod

class ITextSource(ABC):
    @abstractmethod
    def get_text(self) -> str: pass

class ITextInjector(ABC):
    @abstractmethod
    def inject_text(self, text: str) -> None: pass

class ILanguageModelClient(ABC):
    @abstractmethod
    def query(self, prompt: str) -> str: pass

class ITrigger(ABC):
    @abstractmethod
    def listen(self, callback) -> None: pass