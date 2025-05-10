
import logging
from pynput import keyboard as pynput_keyboard
from config import DEBUG_MODE
from core.interfaces import ITrigger

class HotkeyTrigger(ITrigger):
    def __init__(self, hotkey_str: str):
        self.hotkey_str = hotkey_str.lower()

    def listen(self, callback) -> None:
        COMBO = set(self.hotkey_str.split('+'))
        current_keys = set()

        def get_key_name(key):
            try:
                return key.char.lower() if key.char else str(key).replace('Key.', '').lower()
            except AttributeError:
                return str(key).replace('Key.', '').lower()

        def on_press(key):
            k = get_key_name(key)
            current_keys.add(k)
            if DEBUG_MODE:
                logging.info(f'Pressed: {k}, current_keys={current_keys}')
            if COMBO.issubset(current_keys):
                callback()

        def on_release(key):
            k = get_key_name(key)
            current_keys.discard(k)

        listener = pynput_keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()
