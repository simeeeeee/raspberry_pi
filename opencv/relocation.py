import cv2
import numpy as np
points = []
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))
        print(f"Point {len(points)}: {x}, {y}")
    
def warp_image(img, pts):
    w, h = 500, 300 #정사각형으로 변환
    dst_pts = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32) #TL TR BR BL
    matrix = cv2.getPerspectiveTransform(np.array(pts, dtype=np.float32), dst_pts)
    return cv2.warpPerspective(img, matrix, (w, h))

def sort_points(points):
    points = np.array(points, dtype=np.float32)

    # # y 오름차순 (위쪽 먼저)
    # sorted_by_y = points[np.argsort(points[:, 1])]

    # top = sorted_by_y[:2] # 앞 둘
    # bottom = sorted_by_y[2:] # 뒤 둘

    # # Top 중 x 작은 거 → Top-Left, x 큰 거 → Top-Right
    # top = sorted(top, key=lambda p: p[0])
    # top_left, top_right = top

    # # Bottom 중 x 작은 거 → Bottom-Left, x 큰 거 → Bottom-Right
    # bottom = sorted(bottom, key=lambda p: p[0])
    # bottom_left, bottom_right = bottom
    
    # return np.array([top_left, top_right, bottom_right, bottom_left], dtype=np.float32)
    
    sums = points[:, 0] + points[:, 1]
    diffs = points[:, 0] - points[:, 1]

    # argmax(변수) : 어떤 배열에서 (변수)이 가장 큰 값이 있는 위치(인덱스)를 반환하는 함수
    # argmin()
    top_left = points[np.argmin(sums)] # x+y가 최소
    bottom_right = points[np.argmax(sums)] # x+y가 최대
    top_right = points[np.argmax(diffs)] #x-y가 최대
    bottom_left = points[np.argmin(diffs)]#x-y가 최소

    return np.array([top_left, top_right, bottom_right, bottom_left]) #TL, TR, BR, BL 순서 중요!(getPerspectiveTransform()에서 해당 순서)


# 이벤트
img = cv2.imread('saved_image.jpg')
clone = img.copy()
cv2.namedWindow("Select 4 Points")
cv2.setMouseCallback("Select 4 Points", mouse_callback)

while True:
    temp = clone.copy()
    for pt in points:
        cv2.circle(temp, pt, 5, (0, 255, 0), -1)
    cv2.imshow("Select 4 Points", temp)
        
    key = cv2.waitKey(1)
    if key == 27: # ESC
        break
    if len(points) == 4:
        new_points = sort_points(points)
        warped = warp_image(clone, new_points)
        cv2.imshow("Warped", warped)
        
cv2.destroyAllWindows()