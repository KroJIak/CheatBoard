
from PIL import ImageGrab, ImageEnhance
import pytesseract
import logging
from config import DEBUG_MODE
from core.interfaces import ITextSource

class ScreenshotOCRTextSource(ITextSource):
    def get_text(self) -> str:
        screenshot = ImageGrab.grab()
        width, height = screenshot.size
        cropped = screenshot.crop((50, 100, width - 50, height - 50))
        gray = cropped.convert('L')
        contrast = ImageEnhance.Contrast(gray).enhance(2.0)
        bw = contrast.point(lambda x: 0 if x < 215 else 255, '1')
        bw.save("processed_output.png")
        text = pytesseract.image_to_string(bw, lang='eng', config='--psm 6')
        if DEBUG_MODE:
            logging.info(f"OCR (processed) text: {text}")
        return text