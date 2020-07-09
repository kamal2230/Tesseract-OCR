try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
t=pytesseract.image_to_string(Image.open("Tactii.png"))
t=t.replace("v ","")
print(t)