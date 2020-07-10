import pandas as pd
from flask import Flask
from flask import app, render_template

# creates a Flask application, named app
# run the application
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
for i in range(1,len(lis)):
    lis[i]=lis[i].split(" ")
lis[0]=("".join(lis[0])).split("$")
df=pd.DataFrame(lis[1:],columns=lis[0])  
print(df)
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message=df
    return render_template('index.html', message=message)
if __name__ == "__main__":
    app.run(debug=True,port=3000)
