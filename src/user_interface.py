import os
import random

import color_engine
from rich import print

   
def colorPickerUI(img_path: str, num_palettes: int) -> tuple:
#display the selected color scheme and ask user if they like it or want to generate a new color scheme
    hex_colors, hex_compliments = selectPalette(img_path, num_palettes) 
    final_colors, final_compliments = selectColorsFromPalette(hex_colors, hex_compliments)
    return final_colors, final_compliments

def selectPalette(img_path: str, num_palettes: int) -> tuple:
    # 
    confirmed = False
    while not confirmed:
        print()
        popularColors = color_engine.grabColors(img_path, num_palettes)
        hex_colors = color_engine.rgbToHex(popularColors)
        hex_compliments = color_engine.compColors(hex_colors)
        constrast_levels = color_engine.checkContrast(hex_colors, hex_compliments)
        main_colors = ''
        complimentary_colors = ''

        for color in hex_colors:
           main_colors += f'[on {color}]   [/on {color}]' 
        print(main_colors)
        for color in hex_compliments:
           complimentary_colors += f'[on {color}]   [/on {color}]' 
        print(complimentary_colors, '\n')
        count = 0
        for i in range(len(hex_colors)):
            print(f'[{hex_compliments[i]} on {hex_colors[i]}]\tGenerated Color Scheme\t\t ({count})', f'contrast: {constrast_levels[i]}')
            count += 1
        print('[bold](a)ccept palette (g)enerate new palette')
        response = input('> ')
        if response == 'a':
            confirmed = True
            print('[bold green]Palette Confirmed!')
        else:
            continue

    return hex_colors, hex_compliments

def selectColorsFromPalette(hex_colors, hex_compliments):
    selected = False
    while not selected:
        print('[bold blue]Select top 3 colors from list in order Primary, Secondary, Accent (IE, "4 10 6")')
        selectedColors = input("> ")
        selectedColors = selectedColors.split()
        all_digits = all(i.isdigit() for i in selectedColors)
        if all_digits:
            selected = True
        else:
            print('[bold red]Invalid selection. Use positive integers corresponding to color pair to select.')
            continue

    selectedColors = [int(i) for i in selectedColors] 
    final_colors = []
    final_compliments = []
    
    for selection in selectedColors:
        final_colors.append(hex_colors[selection]) 
        final_compliments.append(hex_compliments[selection])

    return final_colors, final_compliments

def pickRandomWallpaper(walls_dir) -> str:
    confirmed = False
    history = []
    num_wallpapers = len(os.listdir(walls_dir))
    while not confirmed:
        if len(history) == num_wallpapers:
            print('[bold blue] Wallpapers exhausted. Resetting history...')
            history.clear()
        wallpaper = walls_dir + random.choice(os.listdir(walls_dir))
        if wallpaper in history:
            continue
        history.append(wallpaper)
        # TODO: Replace image preview with something native to python
        # (Currently borrowing viu module from Rust)
        os.system(f'viu {wallpaper}')
        print(f'picked wallpaper: {wallpaper}')
        print('[bold](a)ccept (r)etry')
        response = input('>')
         
        if response == 'a':
            confirmed = True

    return wallpaper
