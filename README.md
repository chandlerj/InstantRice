# Dynamic Theme Switcher

This program will take in an image and generate a color palette based on the image. This palette will be determined by first doing a KMeans analysis on the image to find the most prominent colors, and then generating a complimentary color for each of the most prominent colors. After determining the colors, the program will automatically update the colors for i3 and Polybar to the new color scheme. Next, the program will update the background displayed to the image passed in and prompt the user to re-load i3.

## Usage

`python3 newTheme.py [image]`

## Requirements

 - Need Python3 version `> 3.6`
 - `numpy`, `cv2`, and `scipy_learn` module

 ## Installation

 - Clone this repo to a safe place
 - Modify this script to adapt to your configuration
    - With polybar, it is hard to uniquely identify the lines for the colors without knowing the line number, for this reason, the script will look for a specific line number to modify, and depending on your configuration you might have to change these line numbers. I use modified version of the stock config files for `i3` and `polybar`, so if your config is based on the stock config file, no changes *should* be necessary.
 - Update `paths.py` with the appropiate paths to your config files
 - In your `.bashrc`, create an alias to the python script
    - IE, `alias newtheme='python3 /home/chandler/Documents/newColors/newTheme.py'`
 - reload your bash config/open & close your terminal
 - apply a new theme to your system!
