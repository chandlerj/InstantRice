import subprocess
import cv2 as cv
import os

from rich import print

def updatei3Theme(
        config_path: str, 
        img_paths: list[str], 
        colors: list[str], 
        compliments: list[str], 
        update_i3_lock: bool, 
        dmenu: bool,
        lock_img_path: str,
        menu_keybind: str,
        ) -> None:
    
    print('[bold red]Updating i3 color scheme')
    

    update_i3_configuration(config_path, colors, compliments, dmenu, img_paths, menu_keybind)
     
    if update_i3_lock:
        change_i3_lock_img(img_paths[0], lock_img_path)
    
    
    print("[bold red]Restarting i3")
    os.system("i3 restart")


def change_i3_lock_img(img_path: str, lock_img_path):
    img = cv.imread(img_path)
    
    imgHeight, imgWidth, _ = img.shape
    screenWidth, screenHeight = getScreenResolution()
    h_lock_scale = screenWidth / imgWidth
    v_lock_scale = screenHeight / imgHeight
    
    print('[bold red]Creating lock screen')
      
    dim = (int(imgWidth * h_lock_scale), int(imgHeight * v_lock_scale))
    img = cv.resize(img, dim, interpolation= cv.INTER_AREA)
     
    cv.imwrite('lock.png', img)
    os.rename('lock.png', lock_img_path)


def update_i3_configuration(
        config_path: str, 
        colors: list[str], 
        compliments: list[str], 
        dmenu: bool, 
        img_paths: list[str],
        menu_keybind: str,
        ) -> None:
    
    data = ''
    bg_set = False

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
        # update background image
        if not bg_set and "set $bgimage" in line:
            if len(img_paths) > 1:
                for j in range(len(img_paths)):
                    data[i + j] = f'set $bgimage{j} ' + img_paths[j] + '\n'
                bg_set = True
            else: 
                data[i] = 'set $bgimage ' + img_paths[0] + '\n'
        # update i3 lock image        
        if f"bindsym {menu_keybind} exec --no-startup-id dmenu_run" in line:
            if dmenu:
                print('[bold red]Updating Dmenu color scheme')
                data[i] = f"bindsym {menu_keybind} exec --no-startup-id dmenu_run -c -nb '{colors[0]}' -sf '{compliments[0]}' -sb '{colors[1]}' -nf '{compliments[1]}'\n"


    with open(config_path, 'w') as file:
        file.writelines(data)
 

def getScreenResolution() -> tuple:
    output = subprocess.Popen("xdpyinfo | awk '/dimensions:/ { print $2 }'",shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    width = int(resolution[0].decode('UTF-8'))
    height = int(resolution[1].decode('UTF-8'))
    return width, height

