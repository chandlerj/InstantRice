import pytermgui as ptg



appearence_settings = {
        "window_gaps": False,
        "titlebars": False,
        "win_boarders": False,
        "inner_gap_sz": "6",
        "outter_gap_sz": "6",
        "win_boarders_width": "6",
        "i3-font": "default",
        "i3-font-size": "10"
        }

# initialize appearance settings dictionary
def initialize_appearence_settings():
    """
    Read in information from configuration files and update the
    apperaance settings dictionary to the appropiate settings based on the
    configuration currently set in the config file
    """
    pass


# callback functions
def set_window_gaps(state) -> None:
    appearence_settings['window_gaps'] = state

def tui_runner():
    with ptg.WindowManager() as manager:
        #layout = ptg.Layout() 
        #layout.add_slot("Body Left", index=0)
        #layout.add_slot("Body Right", width=0.5, index=1)
    
        i3window = (
            ptg.Window(
                    "[bold]i3 Configuration Settings",
                    ptg.Label("[italic gray]gaps", parent_align=0),
                    ptg.Splitter(
                        ptg.Label(
                            "Window gaps", 
                            parent_align=0
                            ), 
                        ptg.Checkbox(
                            parent_align=2, 
                            callback=set_window_gaps, 
                            checked=appearence_settings["window_gaps"]
                            )
                        ),
                    ptg.InputField(prompt="Inner Gaps: ", value=appearence_settings["inner_gap_sz"]),
                    ptg.InputField(prompt="Outer Gaps: ", value=appearence_settings["outter_gap_sz"]),
                    ptg.Label(""),
                    ptg.Label("[italic gray]Window Boarders", parent_align=0),
                    ptg.Splitter(
                        ptg.Label(
                            "Titlebars", 
                            parent_align=0
                            ), 
                        ptg.Checkbox(
                            parent_align=2
                            )
                        ),
                    ptg.Splitter(ptg.Label("Window Boarders", parent_align=0), ptg.Checkbox(parent_align=2)),
                    ptg.InputField(prompt="Boarder Width: "),
                    ptg.Label(""),
                    ptg.Label("[italic gray]Font", parent_align=0),
                    ptg.InputField(prompt="Font: ", value=appearence_settings["i3-font"]),
                    ptg.InputField(prompt="Font Size: ", value=appearence_settings["i3-font-size"]),
                    ptg.Button("Save Changes")
                      )
                           .set_title("[italic inverse !gradient(60)]i3 Configuration[/!]")
                           )         
        polybar_window = (
            ptg.Window(
                    "[bold]Polybar Configuration Settings",
                    ptg.Label("[italic gray]Font", parent_align=0),
                    ptg.InputField(prompt="Font: ", value=appearence_settings["i3-font"]),
                    ptg.InputField(prompt="Font Size: ", value=appearence_settings["i3-font-size"]),
                    ptg.Label(""),
                    ptg.Label("[italic gray]Modules", parent_align=0),
                    ptg.InputField(prompt="Font: ", value=appearence_settings["i3-font"]),
                    ptg.InputField(prompt="Font Size: ", value=appearence_settings["i3-font-size"]),
    
                    ptg.Button("Save Changes")
                    )
                      .set_title("[italic inverse !gradient(45)]Polybar Configuration"))    
        
        #layout.assign(polybar_window, index=0)
        #layout.assign(i3window, index=1)
        manager.add(i3window)
        manager.add(polybar_window)

tui_runner()
print(appearence_settings)
a_pause = input("this is a pause that should run after the tui is closed > ")
