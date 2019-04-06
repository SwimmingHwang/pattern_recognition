import cv2
import numpy as np

def distg40(img):
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray,127,255,0)

    # 이미지를 28x28 행렬화 하기
    images = np.zeros((28, 28))
    flatten = imgray.flatten() / 255.0

    i = 0
    j = 0
    for i in range(28):
        for j in range(28):
            images[i, j] = "%0.1f" % flatten[28 * i + j]

    # In[68]:


    # print (images)


    # In[72]:


    l = 0
    contact = 0
    flag = 0
    end = 0  # 끝점을 찾으면 반복문 끝나게끔

    for i in range(28):  # 열
        for j in range(28):  # 행
            if (images[j, i] != 0):
                end = 1;
                #print("만나는점", i, j)
                k = j + 1  # 만나는 점 아랫줄을 조사, 만나는 점에서의 선은 좀 불안
                l = i
                for l in range(28 - i):
                    if (images[k, l] == 0 and flag == 0):  # 검정을 만나면
                        flag = 1
                        contact += 1
                    if (images[k, l] != 0):
                        flag = 0
                break;
            if (end == 1):
                break

    #print("검정이 나온 횟수: ", contact)

    if (contact == 1):
        return 4
    if (contact == 2):
        return 0

