import cv2 as cv
import numpy as np

def findNumberofContact(img):

    # (y, x) = (50, 50) 좌표의 픽셀값을 읽어오면 [153  43  36]입니다. 좌표 순서가 y, x 순인 것에 유의하세요.

    # 픽셀값은 [blue, green, red] 값으로 구성되어 있는데 blue가 가장 크기 때문에 이미지에서 파란색으로 보입니다.
    contact = 0
    flag = 0
    for idx in range(28):
        #print(img[idx,14]) #세로 14열
        #print(img[14,idx]) # 가로 14행

        #검정이 아닌 것을 만나고 flag가 0이면 cnt++
        #img[idx,14] != [0,0,0] and flag == 0 ) :

        if ( np.array_equal(img[idx,14],[0,0,0])==False  and flag == 0 ) :
            contact+=1
            flag = 1

        #검정을 만났을 때 flag 0으로 초기화
        if(np.array_equal(img[idx,14],[0,0,0]) ):
            flag = 0

    #print("접점의 개수 : ",contact)
    return contact

# 흰색으로 변경하면 아래 결과 영상처럼 파란색 사각형의 왼쪽 아래에 흰점이 출력됩니다.
#img[50,50] = [255,255,255]
#print(img[50,50])


