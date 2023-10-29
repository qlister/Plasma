import plasma
import machine
from plasma import plasma2040
from pimoroni import RGBLED, Button, Analog
import halloween
import xmas
import spring
import daffodils
import bluebells
import PlasmaLED
from PlasmaLED import POLL_DELAY_MS, TENTH_SEC, ONE_SEC
import ujson

#setting = 'Xmas'
#g = open('settings.txt', 'w')
#ujson.dump( setting, g )
#g.close

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
    machine.lightsleep( POLL_DELAY_MS )
        
    current_count -= 1
    if current_count == 0:
        current_count = CURRENT_COUNT
        print("Current =", sense.read_current(), "A")


    
