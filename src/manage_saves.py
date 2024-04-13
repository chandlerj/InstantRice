from rich import print
from theme import Theme
import json
def save_theme(hex_colors, hex_compliments, wallpaper_location, save_location):
    """
    Save a theme to the disk at a specified location as a json object.
    """ 
    

    theme = Theme(hex_colors, hex_compliments, wallpaper_location)


    with open(save_location, 'w') as file:
        json.dump(theme.toDict(), file)
    print('[bold green]color palette saved successfully')

def load_theme(save_location):
    """
    Load a theme from disk at a specified location
    """
    with open(save_location, 'r') as file:
        data = json.loads(file.read()) 
    return data
