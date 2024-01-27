from rich import print

def updatePolybarTheme(config_path: str, colors: list, compliments: list) -> None:
    print('[bold red]Updating polybar color scheme')
    data = ''
    with open(config_path, 'r') as file:
        data = file.readlines()
    for i,line in enumerate(data):
        #update colors
        if "rice-background =" in line:
            data[i] = 'rice-background = ' + colors[0] + '\n'
        if "rice-background-alt =" in line:
            data[i] = 'rice-background-alt = ' + colors[1] + '\n'
        if "rice-foreground =" in line:
            data[i] = 'rice-foreground = ' + compliments[0] + '\n'
        if "rice-primary =" in line:
            data[i] = 'rice-primary = ' + compliments[1] + '\n'
        if "rice-secondary =" in line:
            data[i] = 'rice-secondary = ' + compliments[2] + '\n'
        if "rice-disabled =" in line:
            data[i] = 'rice-disabled = ' + colors[2] + '\n'
    with open(config_path, 'w') as file:
        file.writelines(data)

def initializePolybarConfig(config_path: str) -> None:
    pass
