import board
import neopixel

class superController:
    DOWN = 144

    def __init__(self, num_lights, color_on = None, color_off = None):
        # State of the lights
        self.num_lights = num_lights
        self.next_light = 0
        self.prev_light = 0
        if color_on is None:
            self.color_on = (255,255,255)
            self.color_off = (0,0,0)
        else:
            self.color_on = color_on
            self.color_off = color_off
        
        # initialize the lights array, turn all lights off
        self.pixels = neopixel.NeoPixel(board.D18,
                                        self.num_lights,
                                        brightness=1,
                                        pixel_order=neopixel.RGB)
        self.pixels.fill((0,0,0))

