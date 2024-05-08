import skullboard
import neopixel
import random
from time import sleep

pixel_num = 493 # number of pixels on the board

pixels = neopixel.NeoPixel(skullboard.D18, pixel_num, brightness = .75, auto_write = False)

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

def rect(x, y, width, height, color):
    for px in range(x, x+width):
        for py in range(y + height):
            if(px in range(29) and py in range(17)):
                light(px, py, color)

# Write a function to draw an image, design, or pattern
def skull(color):
    pixels.fill(OFF)
    rect(9,4,color)
    rect(11,3,9,1)
    rect(12,2,7,1)
    rect(8,6,1,4)
    rect(20,6,1,4)
    rect(10,12,9,1)
    for i in range(4):
        rect(11+i*2,13,1,2)
    for i in range(2):
        rect(11+i*5,6,2,2)
    light(13,9,(0,0,0))
    light(15,9,(0,0,0))
    

#THEALPHABET = [LD["A"], LD["B"], LD["C"], LD["D"], LD["E"], LD["F"], LD["G"], LD["H"], LD["I"], LD["J"], LD["K"], LD["L"], LD["M"], LD["N"], LD["O"], LD["P"], LD["Q"], LD["R"], LD["S"], LD["T"], LD["U"], LD["V"], LD["W"], LD["X"], LD["Y"], LD["Z"], LD["0"], LD["1"], LD["2"], LD["3"], LD["4"], LD["5"], LD["6"], LD["7"], LD["8"], LD["9"]]
def main():
    skull((0,255,0))
    pixels.show()
    
        



if __name__ == '__main__':
    main()