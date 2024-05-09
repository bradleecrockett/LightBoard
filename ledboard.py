
import board
import neopixel
import random
from time import sleep

pixel_num = 493 # number of pixels on the board
HEIGHT = 17
WIDTH = 29
pixels = neopixel.NeoPixel(board.D18, pixel_num, brightness = .90, auto_write = False)

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
    
def light(x, y, color): 
    # Turns coordinates into the pixel number on the board, always pass into this
    # if you want to display anything
    # top left pixel is 0,0
    coord = y * 29 
    if(y%2 == 0): 
        # odd numbered rows are backwards
        coord = x + coord 
    else: 
        # even numbered rows are fowards
        coord = coord - x + 28 
    pixels[coord] = color # sets the pixel
    return 

def makeborder (color): 
    # makes a border around the borders in any color you want
    # top, middle, bottom row
    for i in range (29):
        light(i, 0, color)
        light(i , 8, color)
        light(i, 16, color)
    # sides
    for j in range (16):
        light(0, j, color)
        light(29, j, color)
   
def clear(startX, endX, startY, endY): 
    # clears board in a range, endpoints are included
    for h in range (endY - startY):
        for i in range (endX - startX):
            if(i + startX < 28 and i + startX > 0):
                light(i + startX, h + startY, OFF)
    

# Write a function to draw an image, design, or pattern

 


def main():
    clear(0,WIDTH-1, 0, HEIGHT-1)
    colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
    
    while True:
        color = 0
        
        for col in range(HEIGHT):
            for row in range(WIDTH):
#                 print(row,col)
                light(row, col, random.choice(colors))
#                 pixels.show()
                
            
        pixels.show() # update pixels
        sleep(.01) # wait time between each time the board shifts
        # runs over and over again and NEVER EVER STOPS

        # makeborder(BLUE)
        
        # call your function below
        



if __name__ == '__main__':
    main()
