import cv2 as cv
from sklearn.cluster import KMeans

def grabColors(img_path: str, num_colors: int) -> list:
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
    clt = KMeans(n_clusters=num_colors, n_init='auto')
    clt.fit(img.reshape(-1, 3))
    return clt.cluster_centers_

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

def checkContrast(hex_color_list: list, hex_compliment_list: list) -> list:
    """
    Given the list of colors and their compliments, reutrn a list of the contrast values
    between the colors
    """
    color_list = hexToRGB_list(hex_color_list)
    compliment_list = hexToRGB_list(hex_compliment_list)
    contrast_values = []

    for i, color in enumerate(color_list):
        compliment = compliment_list[i]

        # determine relative luminance of each color
        color_luminence = relativeLuminance(color)
        compliment_luminence = relativeLuminance(compliment)
        value = (max(color_luminence, compliment_luminence) + 0.05) / (min(color_luminence, compliment_luminence) + 0.05)
        contrast_values.append(value)
    return contrast_values


def relativeLuminance(color: list):
    
    threshold = 0.03928 # this whole function is magic constants lol
    channels = []

    for channel in color:
        channel_norm = channel / 255
        if channel_norm <= threshold:
            channels.append(channel_norm / 12.92)
        else:
            channel_val = ((channel_norm + 0.055) / 1.055)**(2.4)
            channels.append(channel_val)
    
    red, green, blue = channels
    luminance = (0.2126 * red) + (0.7152 * green) + (0.0722 * blue)
    return luminance
    


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
    """
    Takes in a list of Hex values and returns a tuple of those colors as rgb values
    """
    hex_value = hex_value.lstrip('#')
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4)) # Magic :DDDDDD

def hexToRGB_list(hex_list: list) -> list:
    colors = []
    for color in hex_list:
        hex_value = color.lstrip('#')
        colors.append(tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))) # Magic :DDDDDD
    return colors

