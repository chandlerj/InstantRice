import cv2 as cv
from sklearn.cluster import KMeans

def grabColors(img_path: str, num_colors: int) -> list():
    """
    Takes in an image, and Number of colors, then returns a list of those colors.
    The list of colors will contain the most prominent colors present in the image.
    img_path - the path where your image lives (IE, /home/chandler/Pictures/moss.png)
    num_colors - the number of colors you need back from the image
    """
    img = cv.imread(img_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    # scale image down by factor of 10 to decrease computation time
    dim = (int(len(img[0])/10), int(len(img)/10))
    img = cv.resize(img, dim, interpolation= cv.INTER_AREA)
    # TODO: implement KMeans clustering from scratch to
    # improve program modularity
    clt = KMeans(n_clusters=num_colors, n_init='auto')
    clt.fit(img.reshape(-1, 3))
    return clt.cluster_centers_

def rgbToHex(input_values: list) -> list:
    """
    Takes in a list of RBG color values and returns a list of those same colors as hex values
    """
    hex_list=[]
    for color in input_values:
        red = int(color[0])
        green = int(color[1])
        blue = int(color[2])
        hex_list.append('#{:02x}{:02x}{:02x}'.format(red, green, blue))
    return hex_list

def hexToRGB(hex_value: str) -> tuple:
    hex_value = hex_value.lstrip('#')
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

def compColors(color_list: list) -> list:
    """
    given a list of colors, generate complimentary colors to contrast the prominent colors.
    return a list of these colors.
    """
    compliments = []
    for color in color_list:
        curr_hex = color[1:] # slice off the # from the hex code
        rgb = (curr_hex[0:2], curr_hex[2:4], curr_hex[4:6])
        comp = ['%02X' % (255 - int(a, 16)) for a in rgb] # magic :D
        compliments.append('#' + ''.join(comp))
    return compliments

