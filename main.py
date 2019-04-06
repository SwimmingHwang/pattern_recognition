#image preprocessing -> recognizing digit -> result

from findHierarchy import *
from preprocessor import *
from findNumberofContact import *
from findCircleLoc import *
from findDiagonalDirection import *
from distg40 import *

for idx in range(10):

    print("정답 : ",idx,end=" ")


    #INPUT 파일 형식 다르게 입력받아서 있는 코드
    if idx == 3 or idx == 7 :
        img = cv2.imread("input_data\\"+"test"+str(idx)+".png",0)
    else :
        img = cv2.imread("input_data\\"+"test" + str(idx) + ".jpg", 0)

    getPreprocessedImage(img) #00_


    #classifier
    input_image = 'output_image.png'
    img = cv2.imread(input_image)
    hierarchy=findHierarchy(img) #01_

    #step 1-----------------------------------------------------------------
    #def f(x): return {1: '12357', 2: '4690',3:'8'}[x]
    def f(x): return {1: 'LEFT', 2: 'RIGHT',3:'8'}[x]
    res = f(hierarchy)

    #1
    if(res=='8'):
        print("8")
        continue


    input_image = 'output_image.png'
    img = cv2.imread(input_image)
    contact=findNumberofContact(img)

    #2


    if(res=='LEFT'):
        #step LEFT 2 (12357)----------------------------------------------
        def f(x): return {1: '1', 2: '7',3:'235'}[x]
        res=f(contact)
        if(res=='1' or res =='7'):
            print(res)
            continue

        #step LEFT 3 (235)-------------------------------------
        if(res=='235'):
            res_235=findDiagonalDirection(img,1)
            if res_235 == 2:
                print(res_235)
                continue
            else:
                print(findDiagonalDirection(img, 2))
                continue
                # step LEFT 3-1 (35)--------------------------------------------
    #3


    elif (res=='RIGHT'):
        #step RIGHT 2 (4690)----------------------------------------------
        def f(x): return {2: '40', 3: '69'}[x]
        res=f(contact)

        #step RIGHT 3-1 (40)----------------------------------
        if(res=='40'):
            print(distg40(img))
        #step RIGHT 3-2 (69)----------------------------------
        elif(res=='69'):
            print(findCircleLoc(img))
