label start:
    show screen travelButton
    menu:
        "Where would you like to start?"
        "From the beginning":
            jump axolotl_intro
        "From the frog":
            jump frog_intro
        "From Olm":
            jump olm_intro
        "View Credits":
            call credits
            jump start
    return