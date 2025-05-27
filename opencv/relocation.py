import cv2
import numpy as np
points = []
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))
        print(f"Point {len(points)}: {x}, {y}")
    
def warp_image(img, pts):
    w, h = 500, 300 #정사각형으로 변환
    dst_pts = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(np.array(pts, dtype=np.float32), dst_pts)
    return cv2.warpPerspective(img, matrix, (w, h))

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
        warped = warp_image(clone, points)
        cv2.imshow("Warped", warped)
        
cv2.destroyAllWindows()