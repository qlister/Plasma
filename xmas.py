import plasma
import machine
#from plasma import plasma2040
from pimoroni import RGBLED, Button
import time
from random import randrange
import PlasmaLED
from PlasmaLED import UPDATES

RED = [255, 0, 0]
ORANGE = [255, 165, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
DIM_RED = [128, 0, 0]
DIM_GREEN = [0, 128, 0]
DIM_BLUE = [0, 0, 128]
WHITE = [255, 255, 255]


class xmas:
    
    led_count = 0
    
    def __init__( self, LEDs ):
        self.led_count = len(LEDs)
        self.LEDs = LEDs
        print("initialising with", self.led_count, "LEDs")
        for i in range( self.led_count ):
            if ( i & 1 ) == 0:
                col = DIM_RED
            else:
                col = DIM_GREEN
            LEDs[i].set_colour( col )
        self.count = randrange( int(UPDATES/10), int(UPDATES*4/10) ) 

    def poll(self):
        self.count -= 1
        if self.count == 0:
            self.count = randrange( int(UPDATES/10), int(UPDATES*4/10) )
            self.LEDs[randrange(self.led_count)].flash( WHITE, int(UPDATES/15) )
        for i in range( self.led_count ):
            self.LEDs[i].poll()


        
            



