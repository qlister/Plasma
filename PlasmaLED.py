

POLL_DELAY_MS = 50    # in ms
TENTH_SEC = int( 1000 / POLL_DELAY_MS / 10 )
ONE_SEC = int( 1000 / POLL_DELAY_MS )
TWO_SEC = int( 2000 / POLL_DELAY_MS )
print( "TenthSec = ", TENTH_SEC )

class LED:

    #poll_time_on = 2
    fadecount = 0
    
    def __init__( self, default, led_strip, pos ):
        self.default_colour = default
        self.flash_colour = None
        self.flashcount = 0
        self.led_strip = led_strip
        self.pos = pos    # LED position
        pass
    
    def print( self ):
        print (self.now_colour)
        
    def set_colour( self, colour ):
        self.default_colour = colour
        self.led_strip.set_rgb( self.pos, self.default_colour[0], self.default_colour[1], self.default_colour[2] ) 
        self.fadecount = 0
        
    def poll( self ):
        if self.flashcount != 0:
            self.flashcount -= 1
            if self.flashcount <= 0:
                self.flashcount = 0
                self.led_strip.set_rgb( self.pos, self.default_colour[0], self.default_colour[1], self.default_colour[2] )
                return 0
            else:
                self.led_strip.set_rgb( self.pos, self.flash_colour[0], self.flash_colour[1], self.flash_colour[2] )
                return 1
            
        if self.fadecount != 0:
            self.default_colour = self.__do_fade( )
            self.led_strip.set_rgb( self.pos, self.default_colour[0], self.default_colour[1], self.default_colour[2] )
            return self.fadecount

    def flash ( self, colour, count ):
        self.flash_colour = colour
        self.flashcount = count

    def init_fade( self, from_colour, to_colour, steps, count ):
        self.from_colour = from_colour
        self.to_colour = to_colour
        self.fade_steps = steps
        self.fadecount = self.fade_steps - count
        
    def __do_fade( self ):
        self.r = int( self.from_colour[0] + ( (self.fade_steps - self.fadecount) * float(self.to_colour[0] - self.from_colour[0]) / float(self.fade_steps) ) )
        self.g = int( self.from_colour[1] + ( (self.fade_steps - self.fadecount) * float(self.to_colour[1] - self.from_colour[1]) / float(self.fade_steps) ) )
        self.b = int( self.from_colour[2] + ( (self.fade_steps - self.fadecount) * float(self.to_colour[2] - self.from_colour[2]) / float(self.fade_steps) ) )
        self.fadecount -= 1
        if self.fadecount <= 0:
            self.fadecount = 0
        return [self.r, self.g, self.b ]

    def get_fade( self ):
        return ( self.from_colour, self.to_colour )
