from gpiozero import Button, Buzzer, LED
import time

btn = Button(2, pull_up=True)
bz = Buzzer(15)
led = LED(3)

def play_round():
    global pressed, st
    pressed = False

    led.on()
    st = time.time()

    # 1초 동안 버튼 누르기 대기
    while time.time() - st < 1:
        if pressed:
            return  # 누른 경우 빠르게 다음 라운드로
        time.sleep(0.01)

    # 1초 지나도 안 누른 경우
    if not pressed:
        print("씰퍠")
        led.off()

def on_press():
    global st, pressed

    en = time.time()
    if en - st <= 0.5:
        bz.on()
        time.sleep(0.2)
        bz.off()
        print("썽꽁")
    else:
        print("늦게 눌렀음")

    led.off()
    pressed = True

btn.when_pressed = on_press

# 전체 게임을 30초 동안 반복
start_time = time.time()
while time.time() - start_time < 30:
    play_round()
    time.sleep(0.5)  # 라운드 간 간격 (0.5초)

print("게임 종료!")

