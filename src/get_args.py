import user_interface

def get_args(args):
    if len(args) != 2:
        pass
    elif '-r' in args:
        img_path = user_interface.pickRandomWallpaper()
    else:
        img_path = args[1]
    return img_path
