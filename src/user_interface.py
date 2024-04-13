import os
import random
import color_engine
import manage_saves
from rich import print

   

def colorPickerUI(img_path: str, num_palettes: int) -> tuple:
    """
    display the selected color scheme and ask user if they like it 
    or want to generate a new color scheme
    """
    hex_colors, hex_compliments = selectPalette(img_path, num_palettes) 
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
        os.system(f'viu {wallpaper}')
        print(f'picked wallpaper: {wallpaper}')
        print('[bold](a)ccept (r)etry')
        response = input('>')
         
        if response == 'a':
            confirmed = True

    return wallpaper


def saveThemePrompt(hex_colors, hex_compliments, wallpaper_location, theme_location):
    print('[bold green]Save configuration as preset? (y/n)')
    do_save = input('>')
    if do_save == 'y':
        print('[bold green]enter theme name')
        theme_name = input('>')
        theme_path = theme_location + theme_name + ".theme"
        
        manage_saves.save_theme(hex_colors, hex_compliments, wallpaper_location, theme_path, theme_name)
        print(f'[bold green]Theme {theme_name} saved!')


def themeSelector(theme_dir):
    all_themes = manage_saves.getAllThemes(theme_dir)
    num_themes = len(all_themes) - 1 


    for i, theme in enumerate(all_themes): 
        colors = ''
        comp_colors = ''
        for j in range(len(theme['colors'])):
            colors += f'[on {theme['colors'][j]}]  [/on {theme['colors'][j]}]'
            comp_colors += f'[on {theme['comp_colors'][j]}]  [/on {theme['comp_colors'][j]}]'
        print(f'{colors} Theme ({i}): {theme['name']}\n{comp_colors} Wallpaper: {theme['wallpaper']}')
        os.system(f'viu {theme['wallpaper']} -w 50')
    print('[bold green]Select theme (IE, 4)')

    
    while True:
        response = input('>')
        if response.isdigit():
            if int(response) <= num_themes:
                # valid selection
                return all_themes[int(response)]
            else:
                print(f'[bold red]invalid selection, please enter a valid integer [0 - {num_themes}]') 
                continue
        else:
            print(f'[bold red]invalid selection, please enter a valid integer [0 - {num_themes}]') 
            continue

