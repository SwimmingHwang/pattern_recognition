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

input_image = 'test8.jpg'

img = cv2.imread(input_image)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold를 이용하여 binary image로 변환
ret, thresh = cv2.threshold(imgray,127,255,0)

#contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.
contours,image = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1, (0,255,0), 3)

#hierachy는 contours line의 계층 구조
hierachy=len(contours)

print(hierachy)
#for idx in range(len(contours))
#print(len(contours[0]))

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()