import sys
import color_engine
import user_interface
import update_rofi
import update_i3
import update_polybar
from get_args import get_args
from paths import Paths

def main():
    img_path, update_dmenu, i3lock = get_args(sys.argv) 
    hex_colors, hex_compliments = user_interface.colorPickerUI(img_path)

    if 'polybar' in Paths: 
        update_polybar.updatePolybarTheme(Paths['polybar'], hex_colors, hex_compliments)
    if 'rofi' in Paths:
        update_rofi.updateRofiTheme(Paths['rofi'], hex_colors, hex_compliments)
    if 'i3' in Paths:
        generate_i3lock = False if ('--nolock' in sys.argv) else True
        update_i3.updatei3Theme(Paths['i3'], img_path, hex_colors, hex_compliments, generate_i3lock, update_dmenu)
       

    
if __name__ == '__main__':
    main()
