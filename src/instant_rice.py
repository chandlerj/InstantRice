import sys
import user_interface
import update_rofi
import update_i3
import update_polybar
from get_args import get_args,usage
from load_config import systemConfig      

if __name__ == '__main__':

    if len(sys.argv) > 1:
        img_path, update_dmenu, nolock, initialize, reconfigure = get_args(sys.argv) 
        hex_colors, hex_compliments = user_interface.colorPickerUI(img_path)
        config = systemConfig()
        if config.polybar_config != "": 
            update_polybar.updatePolybarTheme(config.polybar_config, hex_colors, hex_compliments)
        if config.rofi_config != "":
            update_rofi.updateRofiTheme(config.rofi_config, hex_colors, hex_compliments)
        if config.i3_config:
            update_i3.updatei3Theme(config.i3_config, img_path, hex_colors, hex_compliments, nolock, config.use_dmenu, config.i3_lock_image)
    else:
        usage(sys.argv)
