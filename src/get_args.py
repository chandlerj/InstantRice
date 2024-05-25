import user_interface
import manage_saves
import os
from rich import print


def get_args(args, walls_dir, theme_dir) -> tuple:
    
    # arguments that can be passed into program
    VALID_ARGS = ['-r', '-p', '--initialize', '--reconfigure']
    
    initialize = False
    reconfigure = False
    theme = None
    img_path = []
    if '-p' in args: # use colors from a theme
        index = args.index('-p')
        isFile = os.path.isfile(args[index + 1])
        if isFile == True:
             theme = manage_saves.load_theme(args[index + 1])
        img_path = grab_images(args, index + 1) 
    elif '-t' in args: # use theme picker ui to select theme
        theme = user_interface.themeSelector(theme_dir)
        img_path = theme['wallpaper'] if type(theme['wallpaper']) == list else list(theme['wallpaper'])
    elif '-r' in args: # create a theme from a random wallpaper
        index = args.index('-r')
        num_wallpapers = len(args) - index
        print(num_wallpapers)
        img_path = user_interface.pickRandomWallpaper(walls_dir, num_wallpapers)
    else:
        img_path = grab_images(args, 1)
    
    # neither of these do anything useful right now
    if '--initialize' in args:
        initialize = True
    if '--reconfigure' in args:
        reconfigure = True
    return img_path, initialize, reconfigure, theme  


def grab_images(args: list[str], offset: int):
    images = []
    for i in range(offset, len(args)):
        img_path = f"{os.getcwd()}/{args[i]}"
        if not os.path.exists(img_path):
            print(f'[bold red]ERROR: invalid image path {os.getcwd()}/{args[i]}')
            exit(2)
        else:
            images.append(img_path)
    return images

def usage(args) -> None:
    print(f"""Instant Rice - An automatic theming utilitiy

Usage: python3 {args[0]} [Relative Image Path] [-r, --initialize, --reconfigure, --dmenu, --nolock]

Example: rice ships.png --dmenu --nolock

Optinal Arguments:
-r              Pick a random image from the wallpaper folder specified in paths.py
--initialize    Check all configurations files are present and written in a way compatible with instant rice
--reconfigure   launch a TUI interface to change configuration settings of DE components (i3, polybar, rofi, etc)
--dmenu         generate configuration for dmenu in i3 configuration (update dmenu keyboard shortcut)
--nolock        skip generating image for i3lock

It is recommended to alias Instant Rice to a convenient command in your shells config.
For bash this would look like

alias rice='/home/chandler/Documents/InstantRice/src/instant_rice.py'

visit chqn.xyz for other projects""")
