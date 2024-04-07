import pickle
from rich import print

def save_color_palette(hex_colors, hex_compliments, save_directory):
    
    colors = (hex_colors, hex_compliments)

    with open(save_directory, 'wb') as file:
        pickle.dump(colors, file, pickle.HIGHEST_PROTOCOL)
        
    print('[bold green]color palette saved successfully')

def load_color_palette(save_location):
    with open(save_location, 'rb') as file:
        try:
            data = pickle.load(file)
        except:
             print('invalid arguments. -p should be followed by a color palette save')
             exit(2)

    return data
