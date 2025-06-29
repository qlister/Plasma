from random import randrange
import PlasmaLED
from PlasmaLED import UPDATES

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
print ('Halloween')        
print (ORANGES)

class halloween:
    
    led_count = 0
    
    def __init__( self, LEDs ):
        self.led_count = len(LEDs)
        self.LEDs = LEDs
        for i in range( self.led_count ):
            self.LEDs[i].init_fade( RED, DIM_ORANGE, randrange( int(UPDATES*3/10), int(UPDATES*4/10)), 0 )
        self.count = randrange(3,20)     

    def poll(self):
        self.count -= 1
        if self.count == 0:
            self.count = randrange(3,20)
            self.LEDs[randrange(self.led_count-1)].flash( RED, 2 )

        # This polls each LED and if the colour needs to be set then it sets it
        for i in range(self.led_count):
            count = self.LEDs[i].poll()
            if count == 0:
                from_colour, to_colour = self.LEDs[i].get_fade()
                self.LEDs[i].init_fade( to_colour, ORANGES[ randrange(0,len(ORANGES)) ], randrange(int(UPDATES*3/10), int(UPDATES)), 0 )




        
            



