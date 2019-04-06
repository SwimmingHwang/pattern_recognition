#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 200 by 200 pixel image
# ( module input image , test data image, 3,7 png image)
#test0.jpg
#test1.jpg
#test2.jpg
#test3.png
#test4.jpg
#test5.jpg
#test6.jpg
#test7.png
#test8.jpg
#test9.jpg


def findHierarchy(img):


    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #threshold를 이용하여 binary image로 변환
    ret, thresh = cv2.threshold(imgray,127,255,0)

    #contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.

    contours,image = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.drawContours(img, contours, -1, (0,255,0), 3)

    #hierachy는 contours line의 계층 구조

    hierachy=len(contours)

    #png인 경우 그대로 (전처리후 png로 )
    print("GET HIERARCHY :",hierachy)

    return hierachy


#if __name__ == "__main__":
#    findHierarchy()
