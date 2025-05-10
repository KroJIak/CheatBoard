
from plyer import notification
import logging
from config import DEBUG_MODE
from core.interfaces import ITextInjector

class NotificationOnlyInjector(ITextInjector):
    def inject_text(self, text: str) -> None:
        notification.notify(
            title="LLM Ответ",
            message=text,
            timeout=5
        )
        if DEBUG_MODE:
            logging.info(f"Notified text: {text}")