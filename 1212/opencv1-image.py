import cv2
'''
pip install opencv-python 설치
가상 뭐시기 만든거 활성화가... 어떻게 하더라...
'''

# 이미지 불러 창 띄우기
# https://pixabay.com/ko/ <- 무료 이미지, 영상

'''
터미널 위치
~/Documents/OPENCV
 -> 폴더 실행 : python 하위폴더/실행시킬 파일.확장자
 => python 1212/opencv1-image.py

 -> 다른 폴더 안 파일 불러오기
 => cap = cv2.VideoCapture("video/dog.mp4")

cd 하위폴더 
~/Documents/OPENCV/1212
 -> 폴더 실행 : python 실행시킬 파일.확장자
 => python opencv1-image.py

 -> 다른 폴더 안 파일 불러오기
 => cap = cv2.VideoCapture("../video/dog.mp4")
'''

# imread(이미지 경로) : 이미지 반환(numpy)
img = cv2.imread("images/candle.jpg")
img2 = cv2.imread("images/candle.jpg", cv2.IMREAD_GRAYSCALE)
# print("img :", img) # numpy 배열 출력

# imshow(윈도우 이름, 읽어온 이미지) : 이미지를 새창으로 열어주는 함수
cv2.imshow("candle images", img)
cv2.imshow("candle images grayscale", img2)

# waitkey(밀리초) : ASCII CODE 반환
# 윈도우가 대기하는 시간초 -> 이후 창 닫힘
# waitkey가 없다면 바로 꺼짐
key = cv2.waitKey(0) # 0이면 무한대기
print('key : ', key)

changeToChar = chr(key)
changeToASCII = ord(changeToChar)
print(f"문자 : {changeToChar}, ASCII CODE : {changeToASCII}")


cv2.destroyAllWindows()

# 이미지 저장, shape 속성 확인
gray_bird = cv2.imread('images/bird.jpg', cv2.IMREAD_GRAYSCALE)
color_bird = cv2.imread('images/bird.jpg', cv2.IMREAD_COLOR)

# shape 속성 : 세로, 가로, (채널값)을 튜플 형태로 반환
# 채널은 gtayscale 사진일 경우는 값이 없다
print("gray_bird image shape", gray_bird.shape) # (640, 640)
print("color_bird image shape", color_bird.shape) # (640, 640, 3)

cv2.imshow('bird gray', gray_bird)
cv2.imshow('bird color', color_bird)

h1, w1 = gray_bird.shape
print('gray height', h1)
print('gray width', w1)

h2, w2, c2 = color_bird.shape
print('color height', h2)
print('color width', w2)
print('color chammel', c2)

h3, w3 = color_bird.shape[:2]
print("color height3", h3)
print("color width3", w3)


cv2.waitKey(0)
cv2.destroyAllWindows()

# imwrite(저장할 경로명, 저장할 이미지)
cv2.imwrite('output/gray_bird.png', gray_bird)  # 저장 안됨 찾아봐