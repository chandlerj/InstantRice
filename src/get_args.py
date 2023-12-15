import user_interface

def get_args(args):

    dmenu = False
    nolock = False

    if '-r' in args:
        img_path = user_interface.pickRandomWallpaper()
    else:
        img_path = args[1]
    
    if '-dmenu' in args:
        dmenu = True
    if '--nolock' in args:
        nolock = True
    return img_path, dmenu, nolock
