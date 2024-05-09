'''
ws2812 leds 5Volt
Data is pin 12 (6th from corner) aka GPIO18
Ground is pin 14 (7th from corner) many more GNDs available
 
'''
import board
import neopixel
import random
from time import sleep

pixel_num = 493 #number of pixels on the board
#snake things
snake_length = 10
apple_here = False
apple_value = 350


pixels = neopixel.NeoPixel(board.D18, pixel_num, brightness = .75, auto_write = False)

# Values for colors are in GRB (for some reason)
GREEN = ((255, 0, 0))
RED = ((0, 255, 0))
BLUE = ((0, 0, 255))
OFF = ((0,0,0))

pixels.fill(OFF) #resets the board after every attempt
pixels.show()

LD = { #Dictionary of how all the letters will look on the LED board, "o" is on, "i" is off
    " ":"iiiii"+
        "iiiii"+
        "iiiii"+
        "iiiii"+
        "iiiii"+
        "iiiii"+
        "iiiii",
    
    "A":"iioii"+
        "ioioi"+
        "oiiio"+
        "ooooo"+
        "oiiio"+
        "oiiio"+
        "oiiio",
    
    "B":"ooooi"+
        "oiiio"+
        "oiiio"+
        "ooooi"+
        "oiiio"+
        "oiiio"+
        "ooooi",
    
    "C":"ioooi"+
        "oiiio"+
        "oiiii"+
        "oiiii"+
        "oiiii"+
        "oiiio"+
        "ioooi",
    
    "D":"ooooi"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "ooooi",
    
    "E":"ooooo"+
        "oiiii"+
        "oiiii"+
        "ooooi"+
        "oiiii"+
        "oiiii"+
        "ooooo",
    
    "F":"ooooo"+
        "oiiii"+
        "oiiii"+
        "ooooi"+
        "oiiii"+
        "oiiii"+
        "oiiii",
    
    "G":"ioooi"+
        "oiiio"+
        "oiiii"+
        "oiiii"+
        "oiioo"+
        "oiiio"+
        "ioooi",
    
    "H":"oiiio"+
        "oiiio"+
        "oiiio"+
        "ooooo"+
        "oiiio"+
        "oiiio"+
        "oiiio",
    
    "I":"ooooo"+
        "iioii"+
        "iioii"+
        "iioii"+
        "iioii"+
        "iioii"+
        "ooooo",
    
    "J":"ooooo"+
        "iioii"+
        "iioii"+
        "iioii"+
        "iioii"+
        "oioii"+
        "oooii",
    
    "K":"oiiio"+
        "oiioi"+
        "oioii"+
        "oooii"+
        "oiioi"+
        "oiiio"+
        "oiiio",
    
    "L":"oiiii"+
        "oiiii"+
        "oiiii"+
        "oiiii"+
        "oiiii"+
        "oiiii"+
        "ooooo",
    
    "M":"oiiio"+
        "ooioo"+
        "oioio"+
        "oioio"+
        "oiiio"+
        "oiiio"+
        "oiiio",
    
    "N":"oiiio"+
        "ooiio"+
        "ooiio"+
        "oioio"+
        "oioio"+
        "oiioo"+
        "oiiio",
    
    "O":"ooooo"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "ooooo",
    
    "P":"ooooi"+
        "oiiio"+
        "oiiio"+
        "ooooi"+
        "oiiii"+
        "oiiii"+
        "oiiii",
    
    "Q":"ooooo"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "ooooo"+
        "iiioi",
    
    "R":"ooooi"+
        "oiiio"+
        "oiiio"+
        "ooooi"+
        "oioii"+
        "oiioi"+
        "oiiio",
    
    "S":"ioooo"+
        "oiiii"+
        "oiiii"+
        "ioooi"+
        "iiiio"+
        "iiiio"+
        "ooooi",
    
    "T":"ooooo"+
        "iioii"+
        "iioii"+
        "iioii"+
        "iioii"+
        "iioii"+
        "iioii",
    
    "U":"oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "ioooi",
    
    "V":"oiiio"+
        "oiiio"+
        "oiiio"+
        "ioioi"+
        "ioioi"+
        "ioioi"+
        "iioii",
    
    "W":"oiiio"+
        "oiiio"+
        "oiiio"+
        "oiiio"+
        "oioio"+
        "oioio"+
        "ioioi",
    
    "X":"oiiio"+
        "oiiio"+
        "ioioi"+
        "iioii"+
        "ioioi"+
        "oiiio"+
        "oiiio",
    
    "Y":"oiiio"+
        "oiiio"+
        "ioioi"+
        "iioii"+
        "iioii"+
        "iioii"+
        "iioii",
    
    "Z":"ooooo"+
        "iiiio"+
        "iiioi"+
        "iioii"+
        "iioii"+
        "ioiii"+
        "ooooo",
    
    "0":"ooooo"+
        "ooiio"+
        "oioio"+
        "oioio"+
        "oioio"+
        "oiioo"+
        "ooooo",
    
    "1":"iiiio"+
        "iiiio"+
        "iiiio"+
        "iiiio"+
        "iiiio"+
        "iiiio"+
        "iiiio",
    
    "2":"ooooo"+
        "iiiio"+
        "iiiio"+
        "ooooo"+
        "oiiii"+
        "oiiii"+
        "ooooo",
    
    "3":"ooooo"+
        "iiiio"+
        "iiiio"+
        "iiooo"+
        "iiiio"+
        "iiiio"+
        "ooooo",
    
    "4":"oiiio"+
        "oiiio"+
        "oiiio"+
        "ooooo"+
        "iiiio"+
        "iiiio"+
        "iiiio",
    
    "5":"ooooo"+
        "oiiii"+
        "oiiii"+
        "ooooo"+
        "iiiio"+
        "iiiio"+
        "ooooo",
    
    "6":"ooooo"+
        "oiiii"+
        "oiiii"+
        "ooooo"+
        "oiiio"+
        "oiiio"+
        "ooooo",
    
    "7":"ooooo"+
        "iiiio"+
        "iiiio"+
        "iiiio"+
        "iiiio"+
        "iiiio"+
        "iiiio",
    
    "8":"ooooo"+
        "oiiio"+
        "oiiio"+
        "ooooo"+
        "oiiio"+
        "oiiio"+
        "ooooo",
    
    "9":"ooooo"+
        "oiiio"+
        "oiiio"+
        "ooooo"+
        "iiiio"+
        "iiiio"+
        "ooooo",
    
    "!":"oiiii"+
        "oiiii"+
        "oiiii"+
        "oiiii"+
        "oiiii"+
        "iiiii"+
        "oiiii",
    
    ".":"iiiii"+
        "iiiii"+
        "iiiii"+
        "iiiii"+
        "iiiii"+
        "iiiii"+
        "oiiii",
        
    "?":"ioooi"+
        "oiiio"+
        "iiioi"+
        "iioii"+
        "iioii"+
        "iiiii"+
        "iioii",
}
    
def light(x, y, color): #Turns coordinates into the pixel number on the board, always pass into this
    # if you want to display anything
    # top left pixel is 0,0
    coord = y * 29 
    if(y%2 == 0): #odd numbered rows are backwards
        coord = x + coord 
    else: #even numbered rows are fowards
        coord = coord - x + 28 
    pixels[coord] = color #sets the pixel
    return # for no reason

def makeBoarder (color): #makes a border around the borders in any color you want
    #top, middle, bottom row
    for i in range (29):
        light(i, 0, color)
        light(i , 8, color)
        light(i, 16, color)
    #sides
    for j in range (16):
        light(0, j, color)
        light(29, j, color)
   
def stringToDisplay(string, color, w, h, startX, startY):
    for f in range(w):
        for g in range(h):
            if (string[g*w + f] == "o") and f + startX < 28 and g + startY < 17 and f + startX > 0 and g + startY > 0:
                light(f + startX, g + startY, color) #makes sure it is within the board and then displays the letter entered

def moveLetterX(startX, startY, w, h, stringArr, color, stringArr2, color2):
    #moves words across the board top & bottom @ the same time
    stop = startX + len(stringArr) * w + len(stringArr) #determines how many loops you need to run
    #determines which string is longer
    if(len(stringArr) > len(stringArr2)): 
        maxLen = len(stringArr)
    else:
        maxLen = len(stringArr2)
    for f in range (stop): #how many times you need to move 1 over
        for x in range(maxLen): #how many letters there are
            if (x < len(stringArr)): #display top
                stringToDisplay(stringArr[x], color, w, h, startX - f - w + 6 * x, startY)
            if (x < len(stringArr2)):  #display bottom
                stringToDisplay(stringArr2[x], color2, w, h, startX - f - w + 6 * x, startY + 8)
            #sleep(1)
        pixels.show() #update pixels
        sleep(.05) #wait time between each time the board shifts
        for y in range(maxLen): #clears the board so the letters can be made again
            clear(startX - f - w + 6 * y, startX - f + 6 * y, startY, startY + h)
            clear(startX - f - w + 6 * y, startX - f + 6 * y, startY + 8, startY + 8 + h)
        
        
def clear(startX, endX, startY, endY): #clears board in a range, endpoints are included
    for h in range (endY - startY):
        for i in range (endX - startX):
            if(i + startX < 28 and i + startX > 0):
                light(i + startX, h + startY, OFF)
                
def scroll(str): #turns a string into the pixel letters in the dictionary in an array
    out = []
    for l in str.upper():
        out.append(LD[l])
    return out #not useless

    

makeBoarder(BLUE) #dododododod inspector boarder dododoododo

#THEALPHABET = [LD["A"], LD["B"], LD["C"], LD["D"], LD["E"], LD["F"], LD["G"], LD["H"], LD["I"], LD["J"], LD["K"], LD["L"], LD["M"], LD["N"], LD["O"], LD["P"], LD["Q"], LD["R"], LD["S"], LD["T"], LD["U"], LD["V"], LD["W"], LD["X"], LD["Y"], LD["Z"], LD["0"], LD["1"], LD["2"], LD["3"], LD["4"], LD["5"], LD["6"], LD["7"], LD["8"], LD["9"]]
num = 0
while True: #runs over and over again and NEVER EVER STOPS\
    if (num % 2 == 0):
        moveLetterX(28, 1, 5, 7, scroll("Welcome to the RHS"), RED, scroll("     CTE Capstone Showcase"), GREEN)
          
    else:
        moveLetterX(28, 1, 5, 7, scroll("PLTW BioMedical & Engineering"), BLUE, scroll("CTE Computer Science"), GREEN)

    
#moveLetterX(1, 1, 5, 7, LD["O"], RED)
'''
#snake
#its a snake game that runs automaticallyu
#i made it in like 30 minutes but its important trust dont delete it
#not telling you how it works because i will carry the secret to my grave
#(its not that hard to figure out)
while True:
    for f in range(98):
            pixels[f*5] = (100, 200, 0)
    for i in range (pixel_num):
        pixels[i] = (255, 0, 0)
        pixels.show()
        sleep(.005)
        pixels[(i - snake_length+pixel_num)%pixel_num] = (0, 0, 0)
        if (i == apple_value):
            snake_length = snake_length + 1
            apple_here = False
        if (apple_here == False):
            good_choice = False
            while(not good_choice):
                choice = random.randint(0, pixel_num-1)
                if (choice < i - snake_length or choice > i):
                    pixels[choice] = (0, 255, 0)
                    apple_here = True
                    apple_value = choice
                    good_choice = True
        
'''


    

