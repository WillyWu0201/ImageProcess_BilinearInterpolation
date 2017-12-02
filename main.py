from PIL import Image
import numpy as np
import cv2

def openPhoto(name: str):
    return Image.open(name)

def readPhoto(name: str):
    im = cv2.imread(name)
    cv2.imshow('image', im)
    cv2.waitKey(0)

def getFunctionParaOfX():
    a = np.array([[48, 193, 1], [119, 360, 1], [426, 298, 1]])
    b = np.array([428, 421, 751])
    x = np.linalg.solve(a, b)
    return x

def getFunctionParaOfY():
    a = np.array([[48, 193, 1], [119, 360, 1], [426, 298, 1]])
    b = np.array([142, 304, 394])
    y = np.linalg.solve(a, b)
    return y

im1 = openPhoto("108190.jpg")
im2 = openPhoto("108191.jpg")
readPhoto("108190.jpg")
readPhoto("108191.jpg")
X = getFunctionParaOfX()
Y = getFunctionParaOfY()

print(im1.format, im1.size, im1.mode)
print(im2.format, im2.size, im2.mode)
print(X[0], X[1], X[2])
print(Y[0], Y[1], Y[2])
