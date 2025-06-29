from random import randrange
import PlasmaLED
from PlasmaLED import UPDATES
import colours
from colours import SPRING

#RED = [255, 0, 0]
#GREEN = [0, 255, 0]
#BLUE = [0, 0, 255]
#DIM_RED = [128, 0, 0]
#DIM_GREEN = [0, 128, 0]
#DIM_BLUE = [0, 0, 128]
#WHITE = [255, 255, 255]
#YELLOW = [255, 255, 0]

#ORANGE = [255, 165, 0]
#NEON_ORANGE = [255, 95, 31]
#BURNT_ORANGE = [204, 85, 0]
#BRIGHT_ORANGE = [255, 172, 28]
#MAHOGANY = [192, 64, 0]
#RED_ORANGE = [255, 68, 51]
#DIM_ORANGE = [150, 83, 0]

#PALE_BLUE = [0xbe, 0xe3, 0xf3]
#SKY_BLUE = [0x2d, 0xc2, 0xd2]
#GRASS_GREEN = [0xb6, 0xd8, 0x74]
#DAFF_YELLOW = [0xf8, 0xcc, 0x3a] 
#SALMON_PINK = [0xf4, 0x7c, 0x71]

#ORANGES=[ DIM_ORANGE, BURNT_ORANGE, MAHOGANY, RED ]
#SPRING=[ SKY_BLUE, GRASS_GREEN, DAFF_YELLOW, SALMON_PINK ]
#DIM_SPRING = SPRING


class spring:
    
    led_count = 0
    
    def __init__( self, LEDs ):
        
        
        print( 'Spring' )
        print (SPRING)

        self.DIM_SPRING = []
        for self.col in SPRING:
            a = ( self.col[0]*0.6, self.col[1]*0.6, self.col[2]*0.6 )		# RGB tuple
            self.DIM_SPRING.append( a )
            #for y in range(len(SPRING[x])):
            #    DIM_SPRING[x][y] = SPRING[x][y] * 0.6
                
        print( 'Dim Spring' )
        print (self.DIM_SPRING)
        
        self.led_count = len(LEDs)
        self.LEDs = LEDs
#        print("initialising with", self.led_count, "LEDs")
        for i in range( self.led_count ):
            self.LEDs[i].init_fade( self.DIM_SPRING[3], self.DIM_SPRING[1], randrange( int(UPDATES*3/10), int(UPDATES*4/10)), 0 )
        self.count = randrange(3,20)     

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
                self.LEDs[i].init_fade( to_colour, self.DIM_SPRING[randrange(0,len(self.DIM_SPRING))], randrange( int(UPDATES*3/10), UPDATES), 0 )

