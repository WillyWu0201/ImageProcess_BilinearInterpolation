from PIL import Image
import numpy as np
import cv2

def getPhoto():
    im1 = Image.open("108190.jpg")
    im2 = Image.open("108191.jpg")

    print(im1.format, im1.size, im1.mode)
    print(im2.format, im2.size, im2.mode)


def getFunctionParaOfX():
    A = np.mat('48,193,1; 119,360,1; 426,298,1')
    b = np.mat('428,421,751').T
    r = np.linalg.solve(A, b)
    print(r)

def getFunctionParaOfY():
    A = np.mat('48,193,1; 119,360,1; 426,298,1')
    b = np.mat('142,304,394').T
    r = np.linalg.solve(A, b)
    print(r)

getPhoto()
getFunctionParaOfX()
getFunctionParaOfY()