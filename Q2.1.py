# This program changes the pixel values of an imported image, and then finds the sum of all red pixel values in an altered image

import time
from PIL import Image

image = Image.open("chapter1.jpg")
img = image.load() # opening image for alteration


## THIS SECTION IS TAKEN FROM THE ASSINGMENT SHEET
current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10



for x in range(0, image.size[0]): # iterate through rows
    for y in range(0, image.size[1]): # iterate through columns
        # change each pixel by adding generated number
        img[x,y] = (img[x,y][0] + generated_number, img[x,y][1] + generated_number, img[x,y][2] + generated_number)


image.save("chapter1out.png") # save new image

image = Image.open("chapter1out.png") # reopen new image
img = image.load()

sum = 0
for x in range(0, image.size[0]): # iterate through rows
    for y in range(0, image.size[1]): # iterate through columns
        sum += img[x,y][0] # adding only red pixel values to sum 

print('Number of red pixels in the new image: ', sum)