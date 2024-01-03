import color_engine

def updateRofiTheme(config_path: str, colors: list, compliments: list) -> None:
    print('[bold red]Updating Rofi color scheme')
    data = ''
    with open(config_path, 'r') as file:
        data = file.readlines()
    bg = color_engine.hexToRGB(colors[1])
    fg = color_engine.hexToRGB(compliments[1])
    lbg = color_engine.hexToRGB(colors[0])
    lfg = color_engine.hexToRGB(colors[0])
    for i,line in enumerate(data):
        if 'background: ' in line and i == 23:
            data[i] = '    background: rgba({}, {}, {}, 70%);\n'.format(bg[0], bg[1], bg[2])
        if 'foreground: ' in line and i == 28:
            data[i] = '    foreground: rgba({}, {}, {}, 100%);\n'.format(fg[0], fg[1], fg[2])
        if 'lightbg: ' in line and i == 12:
            data[i] = '    lightbg: rgba({}, {}, {}, 100%);\n'.format(lbg[0], lbg[1], lgb[2])
        if 'lightfg: ' in line and i == 7:
            data[i] = '    lightfg: rgba({}, {}, {}, 100%);\n'.format(lfg[0], lfg[1], lfg[2])
    with open(config_path, 'w') as file:
        file.writelines(data)

