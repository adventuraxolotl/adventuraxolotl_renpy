define menu = nvl_menu

define narrator = Character(None, kind=nvl)

#Axolotl
define a = Character(
    what_prefix = "{color=#FF526F}\"{/color}",
    what_suffix = "{color=#FF526F}\"{/color}",
    color = "#FF526F", 
    image="axolotl", 
    kind=nvl
    )

#Frog
layeredimage frog:
    attribute sword default
    attribute throne default
    attribute base default

define f = Character(name="Frog", color="#00C592", image="frog", who_prefix="Herzog ", kind=nvl)
define o = Character(name="Olm", color="#9F928D", image="olm", who_prefix="Baron ", kind=nvl)
define l = Character(name="Lungfish", color="#FF1A1A", image="lungfish", who_prefix="Don ", kind=nvl)
define s = Character(name="Salamander", color="#E8E610", image="sal", who_prefix="Commander ", kind=nvl)
define c = Character(name="Caecillian", color="#454397", image="cae", who_prefix="Captain ", kind=nvl)
define t = Character(name="Toad", color="#E1C354", image="toad", who_prefix="Great ", who_suffix=" Council", kind=nvl)
define n = Character(name="Newt", color="#FF8200", image="newt", who_prefix="Countess ", kind=nvl)
#Peeper's text size is smaller than the normal (28), because he's a smol little thing.
define p = Character(name="Spring Peeper", image="peeper", who_prefix="Squire ", what_size=text_size.small, kind=nvl)