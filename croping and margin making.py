import cv2
import os

from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract
path = "C:\img\sample_clear.png"
img = cv2.imread(path)

directory = r'C:\img'
os.chdir(directory)
# img size = (720, 1156, 3)
            #height #width
imgresize = cv2.resize(img,(2312,1440))
cropimg = img[1025:1050,0:1600]
cv2.imshow("img",imgresize)
print(img.shape)
#cv2.imshow("img1.png", img)
cv2.waitKey(0)