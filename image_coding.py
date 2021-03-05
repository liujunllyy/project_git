#coding=utf-8
import pytesseract
from PIL import Image

im=Image.open("c:/shot1.png")
pytesseract.image_to_string()
