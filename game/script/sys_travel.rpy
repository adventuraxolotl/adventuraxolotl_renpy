default dayCount = 1
default travel_active = False
default chosen_location = "axolotl"
default axolotl.available = False
default frog.available = True
default olm.available = True
default peeper.available = False
default newt.available = False

screen travelButton:
    vbox:
        text "Day: [dayCount]"
        textbutton "Travel" action [SensitiveIf(travel_active), Call("sys_travel")]

screen leader_panel:
    frame:
        background "gui/right_panel.png"
        xsize 227
        xalign 0.98
        side "c l r":
            area(0, 0, 600, 1080)
            viewport id "vp":
                fixed:
                    vbox:
                        xalign 0.5
                        spacing 16
                        use leader_button("axolotl")
                        use leader_button("frog")
                        use leader_button("olm")
                        use leader_button("axolotl")
                        use leader_button("frog")
                        use leader_button("olm")
                        use leader_button("axolotl")
                        use leader_button("frog")
                        use leader_button("olm")
            vbar value YScrollValue("vp"):
                unscrollable "hide"
            vbar value YScrollValue("vp"):
                unscrollable "hide"


screen leader_button(leader="axolotl"):
    imagebutton: 
        idle "gui/button/leader_idle_background.png"
        hover "gui/button/leader_selected_background.png"
        selected_idle "gui/button/leader_selected_background.png"
        selected_hover "gui/button/leader_selected_background.png"
        action NullAction()
        foreground Image("gui/icons/icon_" + leader + ".png", align = (0.5, 0.5))

label startAction:
    $ travel_active = False
    return

label endAction:
    $ travel_active = True
    return

label sys_progress_day:
    python:
        dayCount += 1
    return

label sys_travel:
    menu:
        "Who do you want to talk to?"
        "Queen Axolotl" if axolotl.available:
            call axolotl
        "Spring Peeper" if peeper.available:
            call peeper
        "Herzog Frog" if frog.available:
            call frog
        "Baron Olm" if olm.available:
            call olm
        "Countess Newt" if newt.available:
            call newt

    call expression _return

label axolotl:
    scene bg axolotl 
    menu:
        "talk to axolotl":
            "blah"

label frog:
    scene bg frog
    menu:
        "talk to frog":
            "blah"
        "talk to peeper":
            "blah"

label olm:
    scene bg olm
    menu:
        "talk to olm":
            "blah"
        "talk to newt":
            "blah"