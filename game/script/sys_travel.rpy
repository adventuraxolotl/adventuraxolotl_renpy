default dayCount = 1
default travel_active = False

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
        "Where do you want to go?"
        "Kingdom Ambystoma" if not flag_axolotlIntro.seen:
            jump location_axolotl
        "Anura Duchy" if not flag_frogIntro.seen:
            jump location_frog
        "Proteus Fiefdom" if not flag_olmIntro.seen:
            jump location_olm

label location_axolotl:
    if not flag_axolotlIntro.seen:
        jump axolotl_intro
    scene bg axolotl 
    menu:
        "talk to axolotl":
            "blah"

label location_frog:
    if not flag_frogIntro.seen:
        jump frog_intro
    scene bg frog
    menu:
        "talk to frog":
            "blah"
        "talk to peeper":
            "blah"

label location_olm:
    if not flag_olmIntro.seen:
        jump olm_intro 
    scene bg olm
    menu:
        "talk to olm":
            "blah"
        "talk to newt":
            "blah"