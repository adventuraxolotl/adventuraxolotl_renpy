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