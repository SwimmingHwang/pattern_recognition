import tensorflow as tf
import cv2
import numpy as np
import math
from scipy import ndimage

#output pixel 크기 선언
OUTPUT_SIZE = 28
INPUT_SIZE = 200

def getBestShift(img):
    cy,cx = ndimage.measurements.center_of_mass(img)

    rows,cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx,shifty


def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted


def getPreprocessedImage (gray):


    #흑백 이미지로 읽기
    # flag option 0 : 이미지를 grayscale로 받아들입니다.

    #검은색 바탕의 흰글씨로 이진화한 후, 숫자 영역외의 공백을 모두 제거
    (thresh, gray) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV  | cv2.THRESH_OTSU)

    while np.sum(gray[0]) == 0:
        gray = gray[1:]

    while np.sum(gray[:,0]) == 0:
        gray = np.delete(gray,0,1)

    while np.sum(gray[-1]) == 0:
        gray = gray[:-1]

    while np.sum(gray[:,-1]) == 0:
        gray = np.delete(gray,-1,1)

    rows,cols = gray.shape

    #cv2.imwrite("b.png", gray)
    #숫자가 중앙에 오도록 공백을 다시 추가
    if rows > cols:
        factor = 20.0/rows
        rows = 20
        cols = int(round(cols*factor))
        # first cols than rows
        gray = cv2.resize(gray, (cols,rows))
    else:
        factor = 20.0/cols
        cols = 20
        rows = int(round(rows*factor))
        # first cols than rows
        gray = cv2.resize(gray, (cols, rows))

    colsPadding = (int(math.ceil((OUTPUT_SIZE-cols)/2.0)),int(math.floor((OUTPUT_SIZE-cols)/2.0)))
    rowsPadding = (int(math.ceil((OUTPUT_SIZE-rows)/2.0)),int(math.floor((OUTPUT_SIZE-rows)/2.0)))
    gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')

    shiftx,shifty = getBestShift(gray)
    shifted = shift(gray,shiftx,shifty)
    gray = shifted

    cv2.imwrite("output_image.png", gray)


    #이미지를 0~1 사이값을 갖는 크기 784(=28 x 28)의 일차원 배열로 변환
    #flatten = gray.flatten() / 255.0
    #images[i] = flatten


#if __name__ == "__main__":
#    getPreprocessedImage()

