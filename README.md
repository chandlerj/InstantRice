# Dynamic Theme Switcher

This program will take in an image and generate a color palette based on the image. This palette will be determined by first doing a KMeans analysis on the image to find the most prominent colors, and then generating a complimentary color for each of the most prominent colors. After determining the colors, the program will automatically update the colors for i3 and Polybar to the new color scheme. Next, the program will update the background displayed to the image passed in and prompt the user to re-load i3.

## Usage

`newTheme.py [image]`

## Requirements

 - Need Python3 version `> 3.6`
 - `numpy`, `cv2`, and `scipy_learn` module
