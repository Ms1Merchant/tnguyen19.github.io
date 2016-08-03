import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL
import PIL.ImageDraw

#Tulips
#Aradhana Agnihotri & Terry Nguyen

# Open the image file
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'Tulips.jpg')
my_image = PIL.Image.open(filename)

#Crop image to centermost tulip
my_image = my_image.crop( (290,0,666,750) )

#Rotate image 180 degrees
my_image = my_image.rotate(180, expand=False)

# Assign the length and width of my_image to variables for later use
width = my_image.size[0]
length = my_image.size[1]

#Change colors
img = np.array(my_image)
def stripe(img):
    for r in range(445,length):
            for c in range(width):
                if img[r][c][2]<30 and img[r][c][1]<60 and img[r][c][0]>100: 
                    img[r][c]=[204,0,102] # purple
    for r in range(486,670):
            for c in range(150,175):
                if img[r][c][1]<100 and img[r][c][1]>=60 and img[r][c][0]>=225: 
                    img[r][c]=[51,51,255] # blue
    for r in range(560,609):
            for c in range(171,175):
                if img[r][c][1]<100 and img[r][c][1]>=60 and img[r][c][0]>=200: 
                    img[r][c]=[51,51,255] # blue
                    
stripe(img)

fig, axes = plt.subplots(1, 1)
axes.axis('off')
axes.imshow(img, interpolation='none')
axes.set_title('Tulip')
fig.show()