import cv2 
import numpy as np 
img = cv2.imread("C:/Users/koppo/Downloads/Genshin-Impact_Key-Art-EN-920x518.png", 
cv2.IMREAD_GRAYSCALE) 
kernel = np.ones((5,5), np.uint8) 
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel) 
cv2.imshow("Original", img) 
cv2.imshow("Top Hat", tophat) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
