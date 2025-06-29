from random import randrange
import PlasmaLED
from PlasmaLED import UPDATES
import random

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

DAFFODIL_YELLOW = [ 255, 255, 0 ]
DAFFODIL_ORANGE = [ 255, 204, 49 ]
DAFFODIL_STALK = [ 30, 255, 30 ]

PALE_BLUE = [0xbe, 0xe3, 0xf3]
SKY_BLUE = [0x2d, 0xc2, 0xd2]
GRASS_GREEN = [0xb6, 0xd8, 0x74]
DAFF_YELLOW = [0xf8, 0xcc, 0x3a] 
SALMON_PINK = [0xf4, 0x7c, 0x71]

DAFFODILS = [   [ PALE_BLUE, 0.6, 0.01 ]
              , [ RED, 0.6, 0.01 ]
              , [ DAFFODIL_STALK, 0.6, 0.28 ]
              , [ DAFFODIL_YELLOW, 0.8, 0.70 ]
            ]

class daffodils:
    
    led_count = 0
    
    def __init__( self, LEDs ):
        self.led_count = len(LEDs)
        self.LEDs = LEDs
        for i in range( self.led_count ):
            LEDs[i].init_fade( DAFFODILS[0][0], DAFFODILS[0][0], randrange( int(UPDATES*3/10), int(UPDATES*4/10) ), 0 )
        self.count = randrange(3,20)
        for j in range( len(DAFFODILS) ):
            print( j )
            DAFFODILS[j][0][0] = int(DAFFODILS[j][0][0] * DAFFODILS[j][1])
            DAFFODILS[j][0][1] = int(DAFFODILS[j][0][1] * DAFFODILS[j][1])
            DAFFODILS[j][0][2] = int(DAFFODILS[j][0][2] * DAFFODILS[j][1])
            
    def poll(self):

        # This polls each LED and if the colour needs to be set then it sets it
        for i in range(self.led_count):
            count = self.LEDs[i].poll()
            if count == 0:
                # Read the start end ond colours for the last fade because
                # we need the end colour as the start colour for the next fade
                from_colour, to_colour = self.LEDs[i].get_fade()
                # init the fade with the start as the end colour of the previous fade
                # the end colour is a random selection from our array and the fade time is random
                rnd = random.random()
                accum = 0.0
                for j in range( len(DAFFODILS) ):
                    accum = accum + DAFFODILS[j][2]
                    if ( accum > rnd ):
                        from_colour = DAFFODILS[j][0]
                        break
                if j == len(DAFFODILS):
                    print( "OOPS! We didn't select a colour" )
                
                self.LEDs[i].init_fade( to_colour, from_colour, randrange( int(UPDATES*3/10), UPDATES ), 0 )




        
            



