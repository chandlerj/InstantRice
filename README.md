```
 _           _              _          _          
(_)_ __  ___| |_ __ _ _ __ | |_   _ __(_) ___ ___ 
| | '_ \/ __| __/ _` | '_ \| __| | '__| |/ __/ _ \
| | | | \__ \ || (_| | | | | |_  | |  | | (_|  __/
|_|_| |_|___/\__\__,_|_| |_|\__| |_|  |_|\___\___|
```

![desktop with theme switcher](demo.png)
This program will take in an image and generate a color palette based on the image. This palette will be determined by first doing a KMeans analysis on the image to find the most prominent colors, and then generating a complimentary color for each of the most prominent colors. After determining the colors, the program will automatically update the colors for i3 and Polybar to the new color scheme. Next, the program will update the background displayed to the image passed in and prompt the user to re-load i3.

## Usage

`python3 instant_rice.py [image_path] [-r] [--nolock]`
 - `-r`: pick a random image from your `Paths['wallpapers']` directory
 - `--nolock`: bypass generating an i3 lock screen

## Requirements

 - Need Python3 version `> 3.6`
 - `numpy`, `cv2`, and `scipy_learn` module
 - `viu` for displaying wallpaper previews
    - This program can be easily obtained from the Rust package manager using `cargo install viu`

 ## Installation

 - Clone this repo to a safe place
 - Modify this script to adapt to your configuration
    - With Polybar, it is hard to uniquely identify the lines for the colors without knowing the line number, for this reason, the script will look for a specific line number to modify, and depending on your configuration you might have to change these line numbers. I use modified version of the stock config files for `i3` and `polybar`, so if your config is based on the stock config file, no changes *should* be necessary.
 - Update `paths.py` with the appropriate paths to your config files
 - In your `.bashrc`, create an alias to the python script
    - IE, `alias rice='python3 /home/chandler/Documents/newColors/newTheme.py'`
 - reload your bash config/open & close your terminal
 - apply a new theme to your system (Ex: `rice -r`)!

 ## Configuration

 Instant Rice stores the locations of your configuration files alongside other settings in the `paths.py` folder within a python dictionary. Before using the program, verify the directories and settings are configured to your system. 
 below is the default paths directory configured for my system:
 ```
    Paths = {
            'i3': '/home/chandler/.config/i3/config',
            'polybar': '/home/chandler/.config/polybar/config.ini',
            'wallpapers': '/home/chandler/Pictures/papes/',
            'lockscreen': '/home/chandler/.config/i3/'
            }
 ```
