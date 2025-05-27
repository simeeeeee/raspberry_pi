import cv2
import numpy as np
# 1.빈 캔버스 (검정 배경)생성
canvas = np.zeros((600, 800, 3), dtype=np.uint8)

# 2.마우스 콜백 함수 정의
def draw_circle(event, x, y, flags, param):
    #마우스 왼쪽 버튼 눌렸을 때
    if event == cv2.EVENT_LBUTTONDOWN:
        #반지름 10,색은 초록색,채운 원 (-1)
        cv2.circle(canvas, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow("Canvas", canvas) #다시 화면 갱신
    elif event == cv2.EVENT_RBUTTONDOWN:
        #반지름 10,색은 빨간색, 채운 원
        cv2.circle(canvas, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow("Canvas", canvas) #다시 화면 갱신
    elif event == cv2.EVENT_MBUTTONDOWN:
        #반지름 10,색은 파란색, 두께가 1
        cv2.circle(canvas, (x, y), 10, (255,0,0), 2)
        cv2.imshow("Canvas", canvas) #다시 화면 갱신


# 3.창 생성 및 마우스 이벤트 등록
cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", draw_circle)

# 4.메인 루프 (ESC키 입력 시 종료)
while True:
    cv2.imshow("Canvas", canvas)
    key = cv2.waitKey(1)
    if key == 27: # ESC키
        break
cv2.destroyAllWindows()