import cv2
import numpy as np
from preprocessor import *


def findCircleLoc(img):

    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #threshold를 이용하여 binary image로 변환
    ret, thresh = cv2.threshold(imgray,127,255,0)
    contours,image = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    size_contours = len(contours[1])

    arrcon=[]
    for idx in range(size_contours):
        #print(contours[1][idx][0][1])
        num=contours[1][idx][0][1]
        arrcon.append(num)

    #print("최대 좌표 : ",max(arrcon),"  최소 좌표 : ",min(arrcon))

    centerloc=max((arrcon)+min(arrcon))/2

    #0이 위 1이 아래
    if(centerloc <=14):
        return 9 #UP
    else:
        return 6 #DOWN