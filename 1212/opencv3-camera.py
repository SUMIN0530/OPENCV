import cv2 as cv

cap = cv.VideoCapture(0) # 경로명이 아닌 기기 id
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv.imshow('camera', img)
            if cv.waitKey(10) != -1:                     # 10ms동안 키 입력 대기
                cv.imwrite('output/camera-capture.jpg')  # 사진을 저장
                break
cap.release()
cv.destroyAllWindows()