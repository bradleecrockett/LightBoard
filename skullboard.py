from ledboard import *


pixel_num = 493 # number of pixels on the board

pixels = neopixel.NeoPixel(board.D18, pixel_num, brightness = .75, auto_write = False)

# Values for colors are in GRB (for some reason)
GREEN = ((255, 0, 0))
RED = ((0, 255, 0))
BLUE = ((0, 0, 255))
YELLOW = ((255, 255, 0))
CYAN = ((255, 0, 255))
MAGENTA = ((0, 255, 255))
WHITE = ((255, 255, 255))
OFF = ((0,0,0))

pixels.fill(OFF) # resets the board after every attempt
pixels.show()
    



# Write a function to draw an image, design, or pattern
def skull(color):
    pixels.fill(OFF)
    rect(8,6,1,4, color)
    rect(9,4,1,6,color)
    rect(10,12,9,1,color)
    rect(11,3,9,1,color)
    rect(12,2,7,1,color)
    rect(20,6,1,4,color)

    for i in range(4):
        rect(11+i*2,13,1,2,color)
    for i in range(2):
        rect(11+i*5,6,2,2,color)
    light(13,9,(0,0,0))
    light(15,9,(0,0,0))
    

def main():
    skull((0,255,0))
    pixels.show()
    
        



if __name__ == '__main__':
    main()