import plasma
import machine
from plasma import plasma2040
from pimoroni import RGBLED, Button, Analog
import halloween
import xmas
import spring
import PlasmaLED
from PlasmaLED import POLL_DELAY_MS, TENTH_SEC, ONE_SEC


NUM_LEDS = 50

led = RGBLED(plasma2040.LED_R, plasma2040.LED_G, plasma2040.LED_B)
led.set_rgb(0, 0, 0)

button_a = Button(plasma2040.BUTTON_A)
button_b = Button(plasma2040.BUTTON_B)
button_boot = Button(plasma2040.USER_SW)

sense = Analog(plasma2040.CURRENT_SENSE, plasma2040.ADC_GAIN, plasma2040.SHUNT_RESISTOR)

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)

led_strip.start()

LEDs = []
for i in range(NUM_LEDS):
    col = [0, 0, 0]
    LEDs.append( PlasmaLED.LED( col, led_strip, i ) )    # set the default colour

#led_function = halloween.halloween( LEDs )
led_function = xmas.xmas( LEDs )

fn = 0

CURRENT_COUNT = 5 * ONE_SEC

current_count = CURRENT_COUNT

while True:
    if button_a.read():
        while button_a.read():
            pass
        del led_function
        led_function = xmas.xmas( LEDs )

    if button_b.read():
        while button_b.read():
            pass
        del led_function
        led_function =  halloween.halloween( LEDs )
    if button_boot.read():
        while button_boot.read():
            pass
        del led_function
        led_function = spring.spring( LEDs )


    led_function.poll()
    machine.lightsleep( POLL_DELAY_MS )
        
    current_count -= 1
    if current_count == 0:
        current_count = CURRENT_COUNT
        print("Current =", sense.read_current(), "A")


