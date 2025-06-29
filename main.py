import plasma
import time
import machine
from pimoroni import RGBLED, Button, Analog
import halloween
import xmas
import spring
import daffodils
import bluebells
import PlasmaLED
import ujson
from PlasmaLED import UPDATES


# Magic values for Plasma 2040 current sense
# 3A * 0.015Ω = 0.045V
# 0.045V * 50 (gain) = 2.25V maximum
ADC_GAIN = 50
SHUNT_RESISTOR = 0.015

settings = [ "Xmas", "Halloween", "Spring", "Daffodils", "Bluebells"]

g = open('settings.txt', 'r')
setting = ujson.load( g )
print ( 'Read setting from file:', setting )
g.close()

def changeSetting(setting):
    
    for x in range(len(settings)):
        if settings[x] == setting:
            x = x+1
            if x >= len(settings):
                x = 0
            break
    setting = settings[x]
    g = open('settings.txt', 'w')
    ujson.dump( setting, g )
    print("Setting changed to: ", setting)
    return setting

NUM_LEDS = 50

led = RGBLED("LED_R", "LED_G", "LED_B")
led.set_rgb(0, 0, 0)

button_a = Button("BUTTON_A", repeat_time=0)
button_b = Button("BUTTON_B", repeat_time=0)
button_boot = Button("USER_SW", repeat_time=0)

sense = Analog("CURRENT_SENSE", ADC_GAIN, SHUNT_RESISTOR)

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS)

led_strip.start()

LEDs = []
for i in range(NUM_LEDS):
    col = [0, 0, 0]
    LEDs.append( PlasmaLED.LED( col, led_strip, i ) )    # set the default colour

#led_function = halloween.halloween( LEDs )
led_function = bluebells.bluebells( LEDs )

fn = 0

current_count = 0

Change = True

while True:
    
    if Change == True:
        Change = False
        if setting == "Xmas":
            del led_function
            led_function = xmas.xmas( LEDs )
        elif setting == "Halloween":
            del led_function
            led_function =  halloween.halloween( LEDs )
        elif setting == "Spring":
            del led_function
            led_function = spring.spring( LEDs )
        elif setting == "Daffodils":
            del led_function
            led_function = daffodils.daffodils( LEDs )
        elif setting == "Bluebells":
            del led_function
            led_function = bluebells.bluebells( LEDs )
        
    if button_a.read():
        while button_a.read():
            pass
        Change = True
        setting = changeSetting(setting)

    if button_b.read():
        while button_b.read():
            pass
        Change = True
        setting = changeSetting(setting)

    if button_boot.read():
        while button_boot.read():
            pass
        Change = True
        setting = changeSetting(setting)

    led_function.poll()
    #machine.lightsleep( POLL_DELAY_MS )	# This caused the LEDs to flash...!!!
    time.sleep(1.0 / UPDATES)
        
    current_count += 1
    if current_count > UPDATES:		# Print the current once per second
        current_count = 0
        print("Current =", sense.read_current(), "A")


    
