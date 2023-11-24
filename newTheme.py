import sys, os
import random
import numpy as np
import cv2 as cv
from PIL import Image
from sklearn.cluster import KMeans
from paths import Paths
from rich import print 


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

def hexToRGB(hex_value: str):
    hex_value = hex_value.lstrip('#')
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

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

def updatei3Theme(config_path: str, img_path: str, colors: list, compliments: list, lock: bool):
    print('[bold red]Updating i3 color scheme')
    data = ''
    with open(config_path, 'r') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        # update colors
        if "set $bgcolor" in line:
            data[i] = 'set $bgcolor ' + colors[0] + '\n'
        if "set $in-bgcolor" in line:
            data[i] = 'set $in-bgcolor ' + colors[1] + '\n'
        if "set $text" in line:
            data[i] = 'set $text ' + compliments[0] + '\n'
        if "set $indicator" in line:
            data[i] = 'set $indicator ' + colors[2] + '\n'
        if "set $in-text" in line:
            data[i] = 'set $in-text ' + compliments[1] + '\n'
        #update background image
        if "set $bgimage" in line:
            data[i] = 'set $bgimage ' + img_path + '\n'
    
    # update i3lock image, convert to png so it plays nice w i3lock
    if lock:
        print('[bold red]Creating lock screen')
        img = Image.open(img_path)
        img.save(r'/home/chandler/.config/i3/lock.png')
     
    with open(config_path, 'w') as file:
        file.writelines(data)


def updatePolybarTheme(config_path: str, colors: list, compliments: list):
    print('[bold red]Updating polybar color scheme')
    data = ''
    with open(config_path, 'r') as file:
        data = file.readlines()
    for i,line in enumerate(data):
        #update colors
        if "background =" in line and i == 19:
            data[i] = 'background = ' + colors[0] + '\n'
        if "background-alt =" in line and i == 20:
            data[i] = 'background-alt = ' + colors[1] + '\n'
        if "foreground =" in line and i == 21:
            data[i] = 'foreground = ' + compliments[0] + '\n'
        if "primary =" in line and i == 22:
            data[i] = 'primary = ' + compliments[2] + '\n'
        if "secondary =" in line and i == 23:
            data[i] = 'secondary = ' + compliments[3] + '\n'
        if "disabled =" in line and i == 25:
            data[i] = 'disabled = ' + colors[2] + '\n'
    with open(config_path, 'w') as file:
        file.writelines(data)


def updateRofiTheme(config_path: str, colors: list, compliments: list):
    print('[bold red]Updating Rofi color scheme')
    data = ''
    with open(config_path, 'r') as file:
        data = file.readlines()
    bg = hexToRGB(colors[1])
    fg = hexToRGB(compliments[1])
    lbg = hexToRGB(colors[0])
    lfg = hexToRGB(colors[0])
    for i,line in enumerate(data):
        if 'background: ' in line and i == 23:
            data[i] = '    background: rgba({}, {}, {}, 70%);\n'.format(bg[0], bg[1], bg[2])
        if 'foreground: ' in line and i == 28:
            data[i] = '    foreground: rgba({}, {}, {}, 100%);\n'.format(fg[0], fg[1], fg[2])
        if 'lightbg: ' in line and i == 12:
            data[i] = '    lightbg: rgba({}, {}, {}, 100%);\n'.format(lbg[0], lbg[1], lgb[2])
        if 'lightfg: ' in line and i == 7:
            data[i] = '    lightfg: rgba({}, {}, {}, 100%);\n'.format(lfg[0], lfg[1], lfg[2])
    with open(config_path, 'w') as file:
        file.writelines(data)

def pickRandomWallpaper():
    confirmed = False
    while not confirmed:
        wallpaper = Paths['wallpapers'] + random.choice(os.listdir(Paths['wallpapers']))
        os.system(f'viu {wallpaper}')
        print(f'picked wallpaper: {wallpaper}')
        print('[bold](a)ccept (r)etry')
        response = input('>')
         
        if response == 'a':
            confirmed = True

    return wallpaper


def colorPickerUI(img_path: str):
    #display the selected color scheme and ask user if they like it or want to generate a new color scheme
    confirmed = False
    while not confirmed:
        print()
        popularColors = grabColors(img_path, 5)
        hex_colors = rgbToHex(popularColors)
        hex_compliments = compColors(hex_colors)

        main_colors = ''
        complimentary_colors = ''

        for color in hex_colors:
           main_colors += f'[on {color}]   [/on {color}]' 
        print(main_colors)
        for color in hex_compliments:
           complimentary_colors += f'[on {color}]   [/on {color}]' 
        print(complimentary_colors)
        print()

        for i in range(len(hex_colors)):
            print(f'[{hex_compliments[i]} on {hex_colors[i]}]\tGenerated Color Scheme\t\t')
        for i in range(len(hex_colors)):
            print(f'[{hex_colors[i]} on {hex_compliments[i]}]\tGenerated Color Scheme\t\t')

        print('[bold](a)ccept (r)etry')
        response = input('>')
        
        if response == 'a':
            confirmed = True
    return hex_colors, hex_compliments
def main():
    if '-r' in sys.argv:
        img_path = pickRandomWallpaper()
    else:
        img_path = sys.argv[1]
    
    hex_colors, hex_compliments = colorPickerUI(img_path)
    
    updatePolybarTheme(Paths['polybar'], hex_colors, hex_compliments)
    updateRofiTheme(Paths['rofi'], hex_colors, hex_compliments)
    
    if '--nolock' in sys.argv:
        updatei3Theme(Paths['i3'], img_path, hex_colors, hex_compliments, False)
    else:
        updatei3Theme(Paths['i3'], img_path, hex_colors, hex_compliments, True)

    
    # print("Theme changed successfully, please reload i3")
    print("[bold red]Restarting i3")
    os.system("i3 restart")

main()
