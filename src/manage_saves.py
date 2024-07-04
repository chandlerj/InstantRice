from rich import print
import json
import os

class Theme:
    def __init__(self, colors: list[str], comp_colors: list[str], wallpaper: str, name: str):
        self.colors = colors
        self.comp_colors = comp_colors
        self.wallpaper = wallpaper
        self.name = name
    def toDict(self):
        return {
                "name"       : self.name,
                "colors"     : self.colors,
                "comp_colors": self.comp_colors,
                "wallpaper"  : self.wallpaper,
                }


def getAllThemes(theme_dir):
    themes = []
    themes_in_dir = [file for file in os.listdir(theme_dir) if os.path.isfile(os.path.join(theme_dir, file)) and file.endswith('.theme')]

    for file in themes_in_dir:
        theme_location = theme_dir + file
        themes.append(load_theme(theme_location))
    return themes


def save_theme(hex_colors, hex_compliments, wallpaper_location, save_location, theme_name):
    """
    Save a theme to the disk at a specified location as a json object.
    """ 
    
    theme = Theme(hex_colors, hex_compliments, wallpaper_location, theme_name)

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

