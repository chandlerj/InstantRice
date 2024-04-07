import os
import random
import color_engine
from rich import print

   
def colorPickerUI(img_path: str, num_palettes: int, saved_colors = None) -> tuple:
#display the selected color scheme and ask user if they like it or want to generate a new color scheme
    if saved_colors == None:
        hex_colors, hex_compliments = selectPalette(img_path, num_palettes) 
    else:
        hex_colors, hex_compliments = saved_colors
        print(f'[bold green] colors successfully loaded from file')
    final_colors, final_compliments = selectColorsFromPalette(hex_colors, hex_compliments)
    return final_colors, final_compliments

def displayColors(hex_colors: list, hex_compliments: list):
    constrast_levels = color_engine.checkContrast(hex_colors, hex_compliments)
    main_colors = ''
    complimentary_colors = ''

    for color in hex_colors:
       main_colors += f'[on {color}]   [/on {color}]' 
    print(main_colors)
    for color in hex_compliments:
       complimentary_colors += f'[on {color}]   [/on {color}]' 
    print(complimentary_colors, '\n')
    for i in range(len(hex_colors)):
            print(f'[{hex_compliments[i]} on {hex_colors[i]}]\tGenerated Color Scheme\t\t ({i: 3})', f'contrast: {constrast_levels[i]:.2f}')


def selectPalette(img_path: str, num_palettes: int) -> tuple:

    confirmed = False
    hex_colors = None
    hex_compliments = None
    while not confirmed:
        print()
        popularColors = color_engine.grabColors(img_path, num_palettes)
        hex_colors = color_engine.rgbToHex(popularColors)
        hex_compliments = color_engine.compColors(hex_colors)
        displayColors(hex_colors, hex_compliments)
        print('[bold](a)ccept palette (g)enerate new palette')
        response = input('> ')
        if response == 'a':
            confirmed = True
            print('[bold green]Palette Confirmed!')
        else:
            continue

    return hex_colors, hex_compliments

def selectColorsFromPalette(hex_colors: list, hex_compliments: list) -> tuple:
    selectedColors = []
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

def pickRandomWallpaper(walls_dir: str) -> str:
    confirmed = False
    history = []
    num_wallpapers = len(os.listdir(walls_dir))
    wallpaper = ''
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
