
import time
import pyperclip
import pyautogui
import logging
from config import DEBUG_MODE
from core.interfaces import ITextSource

class ClipboardTextSource(ITextSource):
    def get_text(self) -> str:
        pyperclip.copy('')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.3)
        text = pyperclip.paste()
        if DEBUG_MODE:
            logging.info(f"Copied text: {text}")
        return text