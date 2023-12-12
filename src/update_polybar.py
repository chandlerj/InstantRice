

def updatePolybarTheme(config_path: str, colors: list, compliments: list):
    print('[bold red]Updating polybar color scheme')
    data = ''
    with open(config_path, 'r') as file:
        data = file.readlines()
    for i,line in enumerate(data):
        #update colors
        if "background =" in line and i == 19:
            data[i] = 'background = ' + colors[0] + '\n'
        if "background-alt =" in line and i == 20:
            data[i] = 'background-alt = ' + colors[1] + '\n'
        if "foreground =" in line and i == 21:
            data[i] = 'foreground = ' + compliments[0] + '\n'
        if "primary =" in line and i == 22:
            data[i] = 'primary = ' + compliments[1] + '\n'
        if "secondary =" in line and i == 23:
            data[i] = 'secondary = ' + compliments[2] + '\n'
        if "disabled =" in line and i == 25:
            data[i] = 'disabled = ' + colors[2] + '\n'
    with open(config_path, 'w') as file:
        file.writelines(data)

