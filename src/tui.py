import pytermgui as ptg


gapsToggle = ptg.Checkbox(parent_align=2)

with ptg.WindowManager() as manager:
    #layout = ptg.Layout() 
    #layout.add_slot("Body Left", index=0)
    #layout.add_slot("Body Right", width=0.5, index=1)
    i3window = (
        ptg.Window(
                "[bold]i3 Configuration Settings",
                ptg.Label("[italic gray]gaps", parent_align=0),
                ptg.Splitter(ptg.Label("Window gaps", parent_align=0), gapsToggle),
                ptg.InputField(prompt="Inner Gaps: ", value="6"),
                ptg.InputField(prompt="Outer Gaps: "),
                ptg.Label(""),
                ptg.Label("[italic gray]Window Boarders", parent_align=0),
                ptg.Splitter(ptg.Label("Titlebars", parent_align=0), ptg.Checkbox(parent_align=2)),
                ptg.Splitter(ptg.Label("Window Boarders", parent_align=0), ptg.Checkbox(parent_align=2)),
                ptg.InputField(prompt="Boarder Width: "),
                ptg.Button("Save Changes")
                  )
                  .set_title("[italic inverse !gradient(60)]i3 Configuration[/!]")
               )
    polybar_window = (
        ptg.Window(
            "[bold]Polybar Configuration Settings"
            ).set_title("[italic inverse !gradient(45)]Polybar Configuration")
            )    
    #layout.assign(polybar_window, index=0)
    #layout.assign(i3window, index=1)
    manager.add(i3window)
    manager.add(polybar_window)

