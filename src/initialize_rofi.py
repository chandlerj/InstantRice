from rich import print
import os
def initializeRofi() -> None:
    """
    Create a Rofi theme if one is not present with desired defaults to work with InstantRice.
    Will pull source file from data dir
    """    
    print('[bold red]Initializing Rofi Theme')
    
    uname: str = os.getlogin()
    # copy the default config from data to .config
    configPath = f'/home/{uname}/.config/rofi/'
    dirExists = os.path.isdir(configPath)
    if dirExists:
        print('path exists')
        if os.path.exists(f'{configPath}config.rasi'):
            print('config present')
        else:
            # create the rasi config
            pass
    else:
        print('path doesnt exist')
    # add line to rofi config 
    # (this means we need might need to make the rofi config file, and the rofi directory)
    # (it also will be necessary to grab the current user's username to access their .config)
    print(uname)
    print(dirExists)

initializeRofi()
