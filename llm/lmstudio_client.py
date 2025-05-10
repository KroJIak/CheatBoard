
import re
from openai import OpenAI
from config import LLM_BASE_URL, LLM_API_KEY, LLM_MODEL, LLM_TEMPERATURE
from core.interfaces import ILanguageModelClient

class LMStudioClientWrapper(ILanguageModelClient):
    def __init__(self):
        self.client = OpenAI(base_url=LLM_BASE_URL, api_key=LLM_API_KEY)
        self.model = LLM_MODEL

    def query(self, prompt: str) -> str:
        messages = [
            {
                "role": "system",
                "content": (
                    "A question is given on the subject of Software Systems Analysis and Design. "
                    "Reply only with the correct answer (or answers, if there are several) (e.g., 'a) Turing machines'). "
                    "Do not explain. "
                    "Reply strictly in one line."
                )
            },
            {"role": "user", "content": prompt}
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=LLM_TEMPERATURE
        )
        raw_text = response.choices[0].message.content.strip()
        return re.sub(r"<think>.*?</think>", "", raw_text, flags=re.DOTALL).strip()
