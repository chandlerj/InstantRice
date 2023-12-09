import sys
import color_engine
import user_interface
import update_rofi
import update_i3
import update_polybar
from paths import Paths

def main():
    if '-r' in sys.argv:
        img_path = user_interface.pickRandomWallpaper()
    else:
        img_path = sys.argv[1]
    
    hex_colors, hex_compliments = user_interface.colorPickerUI(img_path)
    if 'polybar' in Paths: 
        update_polybar.updatePolybarTheme(Paths['polybar'], hex_colors, hex_compliments)
    if 'rofi' in Paths:
        update_rofi.updateRofiTheme(Paths['rofi'], hex_colors, hex_compliments)
    if 'i3' in Paths:
        update_dmenu = True if ('-dmenu' in sys.argv) else False 
        if '--nolock' in sys.argv:
            update_i3.updatei3Theme(Paths['i3'], img_path, hex_colors, hex_compliments, False, update_dmenu)
        else:
            update_i3.updatei3Theme(Paths['i3'], img_path, hex_colors, hex_compliments, True, update_dmenu)
        

    
if __name__ == '__main__':
    main()
