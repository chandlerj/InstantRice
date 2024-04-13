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
    img_path = ''
    if '-p' in args:
        index = args.index('-p')
        isFile = os.path.isfile(args[index + 1])
        if isFile == True:
             print("reached")
             theme = manage_saves.load_theme(args[index + 1])
    elif '-t' in args:
        theme = user_interface.themeSelector(theme_dir)
        img_path = theme['wallpaper']
    elif '-r' in args:
        img_path = user_interface.pickRandomWallpaper(walls_dir)
    else:
        img_path = f"{os.getcwd()}/{args[1]}"
        if not os.path.exists(img_path) and\
                args[1] not in VALID_ARGS:
            print(f'[bold red]ERROR: invalid image path {os.getcwd()}/{args[1]}')
            exit(2)

    if '--initialize' in args:
        initialize = True
    if '--reconfigure' in args:
        reconfigure = True
    return img_path, initialize, reconfigure, theme  


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
