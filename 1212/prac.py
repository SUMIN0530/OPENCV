#opencv 실습 3
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 이게 화면 크기 조절하는 건가?
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 아래처럼 하니까 캠이 안꺼짐...
if capture.isOpened():
    while cv2.waitKey(10) < 0:
        ret, frame = capture.read()
        if ret:
            cv2.imshow("VideoFrame", frame)
            if cv2.waitKey(25)& 0xFF == ord('q'):
                break

capture.release()
cv2.destroyAllWindows()
