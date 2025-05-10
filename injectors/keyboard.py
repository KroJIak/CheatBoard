
import pyautogui
import logging
from config import DEBUG_MODE
from core.interfaces import ITextInjector

class KeyboardTextInjector(ITextInjector):
    def inject_text(self, text: str) -> None:
        pyautogui.write(text, interval=0.01)
        if DEBUG_MODE:
            logging.info(f"Injected text: {text}")