import numpy as np
import cv2

#2와 3을 구별하기 위한 가로중앙선 아래로의 획방향찾는 함수

def findDiagonalDirection(img,flag):

    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    images = np.zeros((28,28))
    flatten = imgray.flatten() / 255.0

    i = 0
    j = 0
    for i in range(28):
        for j in range(28):
            images [i,j] ="%0.1f"%flatten[28*i+j]

    #2/35를 구별하기 위한 임계값


    #임의로 16
    if flag == 1:
        median = 16
    else :
        median = 8

    for i in range(28):
        if(images[median,i]!=0):
            #print(images[19,i], i,end=" ")
            if(i<14):
                if flag == 1:
                    return 2
                else :
                    return 5
            if(i>14):
                return 3
    return 0
