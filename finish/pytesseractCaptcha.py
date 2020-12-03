# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = Image.open('test.jpg')
img = img.convert('L')
ans = pytesseract.image_to_string(img)
print(ans)