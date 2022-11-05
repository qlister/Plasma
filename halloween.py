import plasma
import machine
from plasma import plasma2040
from pimoroni import RGBLED, Button
import time
from random import randrange
import PlasmaLED
from PlasmaLED import POLL_DELAY_MS, TENTH_SEC, ONE_SEC

RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
DIM_RED = [128, 0, 0]
DIM_GREEN = [0, 128, 0]
DIM_BLUE = [0, 0, 128]
WHITE = [255, 255, 255]
YELLOW = [255, 255, 0]

ORANGE = [255, 165, 0]
NEON_ORANGE = [255, 95, 31]
BURNT_ORANGE = [204, 85, 0]
BRIGHT_ORANGE = [255, 172, 28]
MAHOGANY = [192, 64, 0]
RED_ORANGE = [255, 68, 51]
DIM_ORANGE = [150, 83, 0]

ORANGES=[ DIM_ORANGE, BURNT_ORANGE, MAHOGANY, RED ]

class halloween:
    
    led_count = 0
    
    def __init__( self, LEDs ):
        self.led_count = len(LEDs)
        self.LEDs = LEDs
#        print("initialising with", self.led_count, "LEDs")
        for i in range( self.led_count ):
            LEDs[i].init_fade( RED, DIM_ORANGE, randrange( TENTH_SEC * 3, TENTH_SEC * 4), 0 )
        self.count = randrange(3,20)     

    def poll(self):
        #    count -= 1
        #    if count == 0:
        #        count = randrange(3,20)
        #        LEDs[randrange(NUM_LEDS-1)].flash( RED, 2 )
        #        LEDs[randrange(NUM_LEDS-1)].flash( RED, 2 )
        #        print( len(ORANGES) )

        # This polls each LED and if the colour needs to be set then it sets it
        for i in range(self.led_count):
            count = self.LEDs[i].poll()
            if count == 0:
                from_colour, to_colour = self.LEDs[i].get_fade()
                self.LEDs[i].init_fade( to_colour, ORANGES[ randrange(0,len(ORANGES)) ], randrange( TENTH_SEC * 3, ONE_SEC ), 0 )




        
            



