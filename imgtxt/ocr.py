import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from flask import Flask
from flask import app, render_template
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
filename="imgtxt\static\Tactii.png"
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
t=pytesseract.image_to_string(Image.open(filename))
app = Flask(__name__)
@app.route("/")
def first():
    return render_template('index.html')
@app.route("/hello")
def hello():
    return render_template('sol.html',message=t)
if __name__ == "__main__":
    app.run(debug=True,port=3000)
