define menu = nvl_menu
define narrator = nvl_narrator
define chr_default = Character(
    kind=nvl,
)
define name_only = Character(kind=chr_default)

#Axolotl
define a = Character(
    color = "#FF526F", 
    name = "Queen Axolotl",
    image= "axolotl", 
    kind=chr_default
    )

#Frog
layeredimage frog:
    attribute sword default
    attribute throne default
    attribute base default

define f = Character(
    name="Frog", 
    color="#00C592", 
    image="frog", 
    who_prefix="Herzog ", 
    kind=chr_default
    )

define o = Character(
    name="Olm", 
    color="#9F928D", 
    image="olm", 
    who_prefix="Baron ", 
    kind=chr_default
    )

define l = Character(
    name="Lungfish", 
    color="#FF1A1A", 
    image="lungfish", 
    who_prefix="Don ", 
    kind=chr_default
    )
    
define s = Character(
    name="Salamander", 
    color="#E8E610", 
    image="sal", 
    who_prefix="Commander ", 
    kind=chr_default
    )

define c = Character(
    name="Caecillian", 
    color="#454397", 
    image="cae", 
    who_prefix="Captain ", 
    kind=chr_default
    )
define t = Character(
    name="Toad", 
    color="#E1C354", 
    image="toad", 
    who_prefix="Great ", 
    who_suffix=" Council", 
    kind=chr_default
    )
define n = Character(
    name="Newt", 
    color="#FF8200", 
    image="newt", 
    who_prefix="Countess ", 
    kind=chr_default
    )
#Peeper's text size is smaller than the normal (28), because he's a smol little thing.
define p = Character(
    name="Spring Peeper", 
    image="peeper", 
    who_prefix="Squire ", 
    what_size=text_size.small, 
    kind=chr_default
    )