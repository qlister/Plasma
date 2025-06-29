from random import randrange
import PlasmaLED
from PlasmaLED import UPDATES
import colours
from colours import SUMMER


class summer:
    
    led_count = 0
    
    def __init__( self, LEDs ):
        

        self.SUMMER = colours.SUMMER

        print( 'Summer' )
        print (SUMMER)

        #self.DIM_SPRING = []
        #for self.col in SPRING:
        #    a = ( self.col[0]*0.6, self.col[1]*0.6, self.col[2]*0.6 )		# RGB tuple
        #    self.DIM_SPRING.append( a )
                
        #print( 'Dim Spring' )
        #print (self.DIM_SPRING)

        self.led_count = len(LEDs)
        self.LEDs = LEDs
        for i in range( self.led_count ):
            self.LEDs[i].init_fade( self.SUMMER[3], self.SUMMER[1], randrange( int(UPDATES*3/10), int(UPDATES*4/10)), 0 )
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
                self.LEDs[i].init_fade( to_colour, self.SUMMER[randrange(0,len(self.SUMMER))], randrange( int(UPDATES*3/10), UPDATES), 0 )


