from adafruit_circuitplayground import cp
import time

while True:
    LIMIT = 10
    Light_Delay = .25
    Black = (0, 0, 0)

    for num in range(0, LIMIT):
        cp.pixels[num] = (0, 100, 30)
        time.sleep(Light_Delay)
        cp.pixels[num] = (Black)
        time.sleep(Light_Delay)

    for num in range(LIMIT - 1, -1, -1):
        cp.pixels[num] = (30, 0, 100)
        time.sleep(Light_Delay)
        cp.pixels[num] = (Black)
        time.sleep(Light_Delay)
