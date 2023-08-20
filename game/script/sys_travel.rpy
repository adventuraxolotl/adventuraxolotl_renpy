label sys_travel:
    menu:
        "Where do you want to go?"
        "Kingdom Ambystoma" if not flag_axolotlIntro.seen:
            jump axolotl_intro
        "Anura Duchy" if not flag_frogIntro.seen:
            jump frog_intro
        "Proteus Fiefdom" if not flag_olmIntro.seen:
            jump olm_intro