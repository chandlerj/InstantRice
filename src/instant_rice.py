import sys

import user_interface
import update_rofi
import update_i3
import update_polybar
import initialize_i3
import initialize_rofi
from get_args import get_args,usage
from load_config import systemConfig      
from rich import print
if __name__ == '__main__':

    if len(sys.argv) > 1:
        
        config = systemConfig()
        img_path, initialize, reconfigure, color_save = get_args(sys.argv, config.wallpaper_directory) 
        if initialize:
            initialize_rofi.reconfigureRofi()
            print('[bold green]Initialization Completed. Exiting...')
            exit(0)
        hex_colors, hex_compliments = user_interface.colorPickerUI(img_path, config.num_palettes)
        if config.polybar_config: 
            update_polybar.updatePolybarTheme(config.polybar_config, hex_colors, hex_compliments)
        if config.rofi_config:
            update_rofi.updateRofiTheme(config.rofi_config, hex_colors, hex_compliments)
        if config.i3_config:
            update_i3.updatei3Theme(config.i3_config, img_path, hex_colors, hex_compliments, config.generate_i3_lock, config.use_dmenu, config.i3_lock_image, config.menu_keybind)
    else:
        usage(sys.argv)
