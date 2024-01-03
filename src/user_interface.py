import os
import random
from paths import Paths
import color_engine
from rich import print

   
def colorPickerUI(img_path: str) -> tuple:
#display the selected color scheme and ask user if they like it or want to generate a new color scheme
    confirmed = False
    while not confirmed:
        print()
        popularColors = color_engine.grabColors(img_path, 3)
        hex_colors = color_engine.rgbToHex(popularColors)
        hex_compliments = color_engine.compColors(hex_colors)

        main_colors = ''
        complimentary_colors = ''

        for color in hex_colors:
           main_colors += f'[on {color}]   [/on {color}]' 
        print(main_colors)
        for color in hex_compliments:
           complimentary_colors += f'[on {color}]   [/on {color}]' 
        print(complimentary_colors)
        print()
        count = 0
        for i in range(len(hex_colors)):
            print(f'[{hex_compliments[i]} on {hex_colors[i]}]\tGenerated Color Scheme\t\t ({count})')
            count += 1
        print('[bold](a)ccept (r)etry')
        response = input('> ')
        if response == 'r':
            continue
        else:
            confirmed = True
    return hex_colors, hex_compliments

def pickRandomWallpaper() -> str:
    confirmed = False
    while not confirmed:
        wallpaper = Paths['wallpapers'] + random.choice(os.listdir(Paths['wallpapers']))
        # TODO: Replace image preview with something native to python
        # (Currently borrowing viu module from Rust)
        os.system(f'viu {wallpaper}')
        print(f'picked wallpaper: {wallpaper}')
        print('[bold](a)ccept (r)etry')
        response = input('>')
         
        if response == 'a':
            confirmed = True

    return wallpaper
