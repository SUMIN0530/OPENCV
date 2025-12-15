import cv2

# 영상 윈도우로 띄우기
cap = cv2.VideoCapture("video/dog.mp4")

# cap.get(int 속성의 ID > cv2.[정해진 상수값])
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 1280.0
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 720.0
print(cap.get(cv2.CAP_PROP_FPS)) # 25.0
print(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 411.0
print(cap.get(cv2.CAP_PROP_POS_FRAMES)) # 0.0

cap.set(cv2.CAP_PROP_POS_FRAMES, 300) # 시작점 제어 가능, CAP_PROP_FRAME_COUNT 보다 작은 크기!!
'''
터미널 위치
~/Documents/OPENCV
 -> 폴더 실행 : python 하위폴더/실행시킬 파일.확장자
 => python 1212/opencv1-image.py
 -> 다른 폴더 안 파일 불러오기
 => cap = cv2.VideoCapture("video/dog.mp4")

 ~/Documents/OPENCV/1212
 -> 폴더 실행 : python 실행시킬 파일.확장자
 => python opencv1-image.py
 -> 다른 폴더 안 파일 불러오기
 => cap = cv2.VideoCapture("../video/dog.mp4")
'''

# cap.isOpened() : bool
# 파일이 정상적으로 열렸는지, 카메라 사용시 연결이 됐는지 확인

# cap.read() : ret, frame 값을 반환
# ret : bool, 프레임을 정상적으로 읽었는지 반환
# frame : numpy, 읽어온 영상의 프레임 하나, ret가 false라면 None
# frame은 image 데이터이기 때문에 cv2.imshow()를 통해 화면에 보여줄 수 있음

# cap.release() : 영상 재생이 끝나고 메모리, 카메라 점유 등 자원을 반납

if cap.isOpened():
    while True:
        ret, frame = cap.read()
        
        if not ret: # ret == false (영상을 모두 재생)
            print('불러올 프레임이 없어요ㅠ')
            break

        cv2.imshow('dog video', frame) # 사진에서 img와 동일 

        # waitKey의 숫자에 따라 영상 길이 조절 가능
        # cv2.CAP_PROP_FPS 가 인자로 들어가면 원본 영상의 속도
        if cv2.waitKey(25)& 0xFF == ord('q'): # 정상 속도(25) / q를 누르면 영상 종료
            # 25대신 cv2.CAP_PROP_FPS 가능. 근데 왜 배속으로 나오지??
            break
else:
    print('비디오 파일 열기 불가능')
    
cap.release()
cv2.destroyAllWindows



