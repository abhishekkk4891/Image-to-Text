import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
from PIL import Image 
import tkinter as tk
from tkinter import filedialog

print("Select the image youu want to convert")



root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename()

img = Image.open(image_path)
text = tess.image_to_string(img)

print(text)

file = open(image_path + ".txt", "w")
file.write(text)
file.close 

