"""
Basically what I want this program to dynamically update the colors based on the desktop background
so it will grab colors from the desktop background by finding the most promident colors and then set
the system colors to these colors. I believe there are two major components involved in making this work

i. The part of the program that analyzes an image and determines the most prominent colors
ii. The part of the program that goes into all the configuration files and updates their color schemes
"""
import sys
import numpy as np
import PIL
import cv2 as cv
from sklearn.cluster import KMeans
def grabColors(img_path: str, num_colors: int) -> list():
    """
    Takes in an image, and Number of colors, then returns a list of those colors.
    The list of colors will contain the most prominent colors present in the image.
    img_path - the path where your image lives (IE, /home/chandler/Pictures/moss.png)
    num_colors - the number of colors you need back from the image
    """
    img = cv.imread(img_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    # scale image down by factor of 10 to decrease computation time
    dim = (int(len(img[0])/10), int(len(img)/10))
    img = cv.resize(img, dim, interpolation= cv.INTER_AREA)
    clt = KMeans(n_clusters=num_colors, n_init='auto')
    clt.fit(img.reshape(-1, 3))
    return clt.cluster_centers_

def rgbToHex(input_values):
    """
    Takes in a list of RBG color values and returns a list of those same colors as hex values
    """
    hex_list=[]
    for color in input_values:
        red = int(color[0])
        green = int(color[1])
        blue = int(color[2])
        hex_list.append('#{:02x}{:02x}{:02x}'.format(red, green, blue))
    return hex_list

def compColors(color_list):
    """
    given a list of colors, generate complimentary colors to contrast the prominent colors.
    return a list of these colors.
    """
    compliments = []
    for color in color_list:
        curr_hex = color[1:] # slice off the # from the hex code
        rgb = (curr_hex[0:2], curr_hex[2:4], curr_hex[4:6])
        comp = ['%02X' % (255 - int(a, 16)) for a in rgb]
        compliments.append('#' + ''.join(comp))
    return compliments
def updatei3Colors(config_path: str):
    pass
    """
    Given a list of colors, update the color scheme using the most popular colors
    
    """
popularColors = grabColors('/home/chandler/Pictures/papes/blueyellow.jpg', 5)
hex_colors = rgbToHex(popularColors)
hex_compliments = compColors(hex_colors)
print(hex_colors)
print(hex_compliments)

def main():
    print(sys.argv[0])

main()
