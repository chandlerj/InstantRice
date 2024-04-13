
class Theme:
    def __init__(self, colors, comp_colors, wallpaper):
        self.colors = colors
        self.comp_colors = comp_colors
        self.wallpaper = wallpaper
    def toDict(self):
        return {
                "colors"     : self.colors,
                "comp_colors": self.comp_colors,
                "wallpaper"  : self.wallpaper
                }
