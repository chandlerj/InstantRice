from rich import print
import os
def initializeRofi() -> None:
    """
    Create a Rofi theme if one is not present with desired defaults to work with InstantRice.
    Will pull source file from data dir
    """    
    print('[bold red]Initializing Rofi Theme')
    
    uname = os.getlogin()
    

    # copy the default config from data to .config

    # add line to rofi config 
    # (this means we need might need to make the rofi config file, and the rofi directory)
    # (it also will be necessary to grab the current user's username to access their .config)
    print(uname)

initializeRofi()
