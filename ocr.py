try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
print(pytesseract.image_to_string(Image.open("Tactii.png")))