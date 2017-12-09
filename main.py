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

# 取得六參數(圖ㄧ對應圖二)
def getFunctionParaOfX():
    a = np.array([[428, 142, 1], [421, 304, 1], [751, 394, 1]])
    b = np.array([48, 119, 426])
    x = np.linalg.solve(a, b)
    return x

def getFunctionParaOfY():
    a = np.array([[428, 142, 1], [421, 304, 1], [751, 394, 1]])
    b = np.array([193, 360, 298])
    y = np.linalg.solve(a, b)
    return y

# 取得六參數(圖二對應圖一)
# def getFunctionParaOfX():
#     a = np.array([[48, 193, 1], [119, 360, 1], [426, 298, 1]])
#     b = np.array([428, 421, 751])
#     x = np.linalg.solve(a, b)
#     return x
#
# def getFunctionParaOfY():
#     a = np.array([[48, 193, 1], [119, 360, 1], [426, 298, 1]])
#     b = np.array([142, 304, 394])
#     y = np.linalg.solve(a, b)
#     return y

# 把照片一轉成照片二的座標
def getTransferCoordinate(X, Y, x, y):
    newX = X[0] * x + X[1] * y + X[2]
    newY = Y[0] * x + Y[1] * y + Y[2]
    return (newX, newY)
    # return(int(newX + 0.5), int(newY + 0.5)) # 四捨五入

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

NewPhotoFileName = 'combinePhoto' # 'combineBilinearPhoto'

# 讀入照片
im1 = readPhoto("small246.jpg")
im2 = readPhoto("small247.jpg")

# 算出六參數
X = getFunctionParaOfX()
Y = getFunctionParaOfY()

# 建立一張新照片
newImage = np.zeros((450 * 2, 800 * 2, 3), np.uint8)
height, width, _ = newImage.shape

# 處理新照片
print('start process photo')
for x in range(width):
    for y in range(height):
        if y < 450 and x < 800:
            newImage[y][x] = im1[y][x]
        else:
            newX, newY = getTransferCoordinate(X, Y, x, y)
            if 0 <= newY < 450 and 0 <= newX < 800:
                # newImage[y][x] = im2[newY][newX]
                newImage[y][x] = getBilinearInterpolate(im2, newX, newY)
            else:
                newImage[y][x] = 0
print('process photo done')

savePhoto(NewPhotoFileName, newImage)
showPhoto(NewPhotoFileName)