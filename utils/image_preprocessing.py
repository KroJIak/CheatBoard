
def enhance_image_for_ocr(image):
    from PIL import ImageEnhance
    gray = image.convert('L')
    contrast = ImageEnhance.Contrast(gray).enhance(2.0)
    bw = contrast.point(lambda x: 0 if x < 215 else 255, '1')
    return bw
