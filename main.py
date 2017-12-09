from PIL import Image
import numpy as np
import cv2

# 讀入照片
def readPhoto(name):
    return cv2.imread(name)

# 儲存照片
def savePhoto(name):
    cv2.imwrite( name + '.png', newImage)

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
    return(int(newX + 0.5), int(newY + 0.5)) # 四捨五入

NewPhotoFileName = 'combinePhoto'

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
                # print(newX, newY, x, y)
                newImage[y][x] = im2[newY][newX]
            else:
                newImage[y][x] = 0
print('process photo done')

savePhoto(NewPhotoFileName)
showPhoto(NewPhotoFileName)
