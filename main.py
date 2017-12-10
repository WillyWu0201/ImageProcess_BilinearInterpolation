from PIL import Image
import numpy as np
import cv2

# 讀入照片
def readPhoto(name):
    return cv2.imread(name)

# 儲存照片
def savePhoto(name, im):
    cv2.imwrite( name + '.png', im)

# 打開照片
def showPhoto(image):
    Image.open(image + '.png').show()

# 取得六參數
def getFunctionParaOfX():
    a = np.array([[2418, 67, 1], [1992, 1952, 1], [2896, 1866, 1]])
    b = np.array([601, 177, 1081])
    x = np.linalg.solve(a, b)
    return x

def getFunctionParaOfY():
    a = np.array([[2418, 67, 1], [1992, 1952, 1], [2896, 1866, 1]])
    b = np.array([71, 1958, 1870])
    y = np.linalg.solve(a, b)
    return y

# 轉換座標
def getTransferCoordinate(X, Y, x, y):
    newX = X[0] * x + X[1] * y + X[2]
    newY = Y[0] * x + Y[1] * y + Y[2]
    return (newX, newY)

# 做Bilinear Interpolate
def getBilinearInterpolate(im, x, y):
    x = np.asarray(x)
    y = np.asarray(y)

    x0 = np.floor(x).astype(int)
    x1 = x0 + 1
    y0 = np.floor(y).astype(int)
    y1 = y0 + 1

    x0 = np.clip(x0, 0, im.shape[1] - 1)
    x1 = np.clip(x1, 0, im.shape[1] - 1)
    y0 = np.clip(y0, 0, im.shape[0] - 1)
    y1 = np.clip(y1, 0, im.shape[0] - 1)

    imA = im[y0, x0]
    imB = im[y1, x0]
    imC = im[y0, x1]
    imD = im[y1, x1]

    wa = (x1 - x) * (y1 - y)
    wb = (x1 - x) * (y - y0)
    wc = (x - x0) * (y1 - y)
    wd = (x - x0) * (y - y0)

    result = wa * imA + wb * imB + wc * imC + wd * imD
    return result

# 輸入的檔案名稱
NewPhotoFileName = 'combineBilinearPhoto'

# 讀入照片
im1 = readPhoto("1.jpg")
im2 = readPhoto("2.jpg")

# 算出六參數
X = getFunctionParaOfX()
Y = getFunctionParaOfY()

# 驗證六參數
newX, newY = getTransferCoordinate(X, Y, 2176, 1122)
print(newX, newY)

# 建立一張新照片
newImage = np.zeros((2438, 5430, 3), np.uint8)
height, width, _ = newImage.shape

# 處理新照片
print('start process photo')
for x in range(width):
    for y in range(height):
        if y < 2227 and x < 3147:
            newImage[y][x] = getBilinearInterpolate(im1, x, y)
        else:
            newX, newY = getTransferCoordinate(X, Y, x, y)
            if 0 <= newY < 2227 and 0 <= newX < 3147:
                newImage[y][x] = getBilinearInterpolate(im2, newX, newY)
            else:
                newImage[y][x] = 0
print('process photo done')

savePhoto(NewPhotoFileName, newImage)
showPhoto(NewPhotoFileName)