import pandas as pd
from flask import Flask
from flask import app, render_template
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
filename="static\Tactii.png"
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
t=pytesseract.image_to_string(Image.open(filename))
t=t.replace("v ","")
t=t.replace("Name","name")
t=t.replace("Definition","definition")
lis=list((t.split("\n\n")))
lis[0]=list(lis[0])
for i in range(len(lis[0])):
    if(lis[0][i]==" " and lis[0][i+1].isupper()):
        lis[0][i]="$"
for i in range(1,len(lis)):
    lis[i]=lis[i].split(" ")
lis[0]=("".join(lis[0])).split("$")
df=pd.DataFrame(lis[1:],columns=lis[0])  
print(df)
app = Flask(__name__)
@app.route("/")
def first():
    return render_template('index.html')
@app.route("/hello")
def hello():
    message=t
    return render_template('sol.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
if __name__ == "__main__":
    app.run(debug=True,port=3000)
