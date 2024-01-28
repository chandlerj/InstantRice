import pytermgui as ptg


global gaps_enabled
gaps_enabled = False
def toggle_gaps(gaps):
    gaps = not gaps

with ptg.WindowManager() as manager:
    layout = ptg.Layout() 
    layout.add_slot("Body Left", index=0)
    layout.add_slot("Body Right", width=0.5, index=1)
    i3window = (
        ptg.Window(
                "[bold]i3 Configuration Settings",
                ptg.Label("[italic gray]gaps", parent_align=0),
                ptg.Splitter(ptg.Label("Toggle window gaps", parent_align=0), ptg.Checkbox(parent_align=2))
                  )
                  .set_title("[italic inverse !gradient(60)]i3 Configuration[/!]")
               )
    polybar_window = (
        ptg.Window(
            "[bold]Polybar Configuration Settings"
            ).set_title("[italic inverse !gradient(45)]Polybar Configuration")
            )    
    layout.assign(polybar_window, index=0)
    layout.assign(i3window, index=1)
    manager.add(i3window)
    manager.add(polybar_window)

