#!/bin/bash
# 1. auto_exposure 끄기 (Manual Mode: 1)
v4l2-ctl -d /dev/video0 --set-ctrl=auto_exposure=1
# 2. exposure_time_absolute 값 150 으로 설정
v4l2-ctl -d /dev/video0 --set-ctrl=exposure_time_absolute=1500
# 3. gain 값 100 으로 설정
v4l2-ctl -d /dev/video0 --set-ctrl=gain=100
# 4. contrast 값 50 으로 설정
v4l2-ctl -d /dev/video0 --set-ctrl=contrast=50
# 5. while_balance_automatic 끄기
v4l2-ctl -d /dev/video0 --set-ctrl=white_balance_automatic=0
# 6. while_balace_temperature 조절
v4l2-ctl -d /dev/video0 --set-ctrl=while_balance_temperature=7000
# 5. gst-launch-1.0 실행 (카메라 스트림 출력)
gst-launch-1.0 -v \
v4l2src device=/dev/video0 ! \
image/jpeg,width=1280,height=720,framerate=30/1 ! \
jpegdec ! \
videoconvert ! \
autovideosink
