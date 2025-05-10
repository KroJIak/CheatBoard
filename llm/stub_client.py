
from core.interfaces import ILanguageModelClient

class StubClient(ILanguageModelClient):
    def query(self, prompt: str) -> str:
        return f"[Mocked answer to]: {prompt.strip()[:60]}..."
