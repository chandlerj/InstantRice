import subprocess
import cv2 as cv
import os

from rich import print
from paths import Paths

def updatei3Theme(config_path: str, img_path: str, colors: list, compliments: list, lock: bool, dmenu: bool) -> None:
    print('[bold red]Updating i3 color scheme')
    data = ''
    with open(config_path, 'r') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        # update colors
        if "set $bgcolor" in line:
            data[i] = 'set $bgcolor ' + colors[0] + '\n'
        if "set $in-bgcolor" in line:
            data[i] = 'set $in-bgcolor ' + colors[1] + '\n'
        if "set $text" in line:
            data[i] = 'set $text ' + compliments[0] + '\n'
        if "set $indicator" in line:
            data[i] = 'set $indicator ' + colors[2] + '\n'
        if "set $in-text" in line:
            data[i] = 'set $in-text ' + compliments[1] + '\n'
        #update background image
        if "set $bgimage" in line:
            data[i] = 'set $bgimage ' + img_path + '\n'
        
        if "bindsym $mod+d exec --no-startup-id dmenu_run" in line:
            if dmenu:
                print('[bold red]Updating Dmenu color scheme')
                data[i] = f"bindsym $mod+d exec --no-startup-id dmenu_run -nb '{colors[0]}' -sf '{compliments[0]}' -sb '{colors[1]}' -nf '{compliments[1]}'\n"
    # update i3lock image, convert to png so it plays nice w i3lock
    if lock:
        img = cv.imread(img_path)
        imgHeight, imgWidth, _ = img.shape
        screenWidth, screenHeight = getScreenResolution()
        lock_scale = screenWidth / imgWidth
        print('[bold red]Creating lock screen')
        dim = (int(imgWidth * lock_scale), int(imgHeight * lock_scale))
        img = cv.resize(img, dim, interpolation= cv.INTER_AREA)
        cv.imwrite('lock.png', img)
        os.rename('lock.png', Paths['lockscreen'] + 'lock.png')
    with open(config_path, 'w') as file:
        file.writelines(data)
   
    print("[bold red]Restarting i3")
    os.system("i3 restart")


def getScreenResolution() -> tuple:
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    width = int(resolution[0].decode('UTF-8'))
    height = int(resolution[1].decode('UTF-8'))
    return width, height

