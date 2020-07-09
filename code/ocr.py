try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
t=pytesseract.image_to_string(Image.open("Tactii.png"))
t=t.replace("v ","")
t=t.replace("Name","name")
t=t.replace("Definition","definition")
lis=list((t.split("\n\n")))
lis[0]=list(lis[0])
for i in range(len(lis[0])):
    if(lis[0][i]==" " and lis[0][i+1].isupper()):
        lis[0][i]="$"
lis[0]=("".join(lis[0])).split("$")
print(lis)