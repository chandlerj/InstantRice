import sys
import user_interface
import update_rofi
import update_i3
import update_polybar
from get_args import get_args,usage
from paths import Paths
      
if __name__ == '__main__':
    if len(sys.argv) > 1:
        img_path, update_dmenu, nolock, initialize, reconfigure = get_args(sys.argv) 
        hex_colors, hex_compliments = user_interface.colorPickerUI(img_path)
         
        if 'polybar' in Paths: 
            update_polybar.updatePolybarTheme(Paths['polybar'], hex_colors, hex_compliments)
        if 'rofi' in Paths:
            update_rofi.updateRofiTheme(Paths['rofi'], hex_colors, hex_compliments)
        if 'i3' in Paths:
            update_i3.updatei3Theme(Paths['i3'], img_path, hex_colors, hex_compliments, nolock, update_dmenu)
    else:
        usage(sys.argv)
