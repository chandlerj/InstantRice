from rich import print
import os

uname: str = os.getlogin()
configPath = f'/home/{uname}/.config/rofi/'

def reconfigureRofi() -> None:
    """
    Create a Rofi configuration file if one is not present with desired defaults to work with InstantRice.
    """    
    print('[bold red]Initializing Rofi Theme')
    
    def changeConfigContents() -> None:
        print('path exists')
        if os.path.exists(f'{configPath}config.rasi'):
            print('config present')
            with open(f'{configPath}config.rasi', 'r') as file:
                data = file.readlines()
            themeSet = False
            for i, line in enumerate(data):
                if '@theme' in line:
                    themeSet = True
                    data[i] = '@theme "theme.rasi"'
            if not themeSet:
                data.append('@theme "theme.rasi"')
            with open(f'{configPath}config.rasi', 'w') as file:
                file.writelines(data)
        else:
            # create the rasi config
            file = open(rf'{configPath}config.rasi', 'w')
            file.write('@theme "theme.rasi"')
            file.close()

    # copy the default config from data to .config
    dirExists = os.path.isdir(configPath)
    if dirExists:
        changeConfigContents()
    else:
        print('path doesnt exist')


def dropRofiTheme():
    """
    Drop the config file from data/ directory and place it in the .config/rofi directory
    """
    with open('../data/theme.rasi', 'r') as file:
        data = file.readlines()

    with open(f'{configPath}theme.rasi', 'w') as file:
        file.writelines(data)
    

reconfigureRofi()
dropRofiTheme()
