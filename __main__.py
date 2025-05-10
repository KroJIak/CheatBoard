
from app import LLMInjectorApp
from core.triggers.hotkey import HotkeyTrigger
from sources.clipboard import ClipboardTextSource
from sources.screenshot_ocr import ScreenshotOCRTextSource
from injectors.keyboard import KeyboardTextInjector
from injectors.notify import NotificationOnlyInjector
from llm.lmstudio_client import LMStudioClientWrapper
from llm.stub_client import StubClient
import time
from threading import Thread

import logging
from config import DEBUG_MODE

if DEBUG_MODE:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s"
    )


def run_all():
    apps = [
        LLMInjectorApp(HotkeyTrigger('ctrl+alt+n'), ClipboardTextSource(), LMStudioClientWrapper(), KeyboardTextInjector()),
        LLMInjectorApp(HotkeyTrigger('ctrl+alt+m'), ScreenshotOCRTextSource(), LMStudioClientWrapper(), KeyboardTextInjector()),
        LLMInjectorApp(HotkeyTrigger('ctrl+alt+b'), ScreenshotOCRTextSource(), LMStudioClientWrapper(), NotificationOnlyInjector()),
        LLMInjectorApp(HotkeyTrigger('ctrl+alt+v'), ClipboardTextSource(), LMStudioClientWrapper(), NotificationOnlyInjector()),

        LLMInjectorApp(
            HotkeyTrigger('ctrl+alt+z'),
            ClipboardTextSource(),
            StubClient(),
            NotificationOnlyInjector()
        )
    ]
    for app in apps:
        Thread(target=app.run, daemon=True).start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    run_all()