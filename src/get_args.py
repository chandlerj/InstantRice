import user_interface
import manage_saves
import os
from rich import print
def get_args(args, walls_dir) -> tuple:
    
    # arguments that can be passed into program
    initialize = False
    reconfigure = False
    color_save = None
    VALID_ARGS = ['-r', '-p', '--initialize', '--reconfigure']
    if '-p' in args:
        index = args.index('-p')
        if os.path.isfile(args[index + 1]):
             color_save = manage_saves.load_color_palette(args[index + 1])
        else:
             print('invalid arguments. -p should be followed by a color palette save')
             exit(2)
   
    if '-r' in args:
        img_path = user_interface.pickRandomWallpaper(walls_dir)
    else:
        img_path = f"{os.getcwd()}/{args[1]}"
        if not os.path.exists(img_path) and\
                args[1] not in VALID_ARGS:
            print(f'[bold red]ERROR: invalid image path {os.getcwd()}/{args[1]}')
            exit(3)

    if '--initialize' in args:
        initialize = True
    if '--reconfigure' in args:
        reconfigure = True
    return img_path, initialize, reconfigure, color_save

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
