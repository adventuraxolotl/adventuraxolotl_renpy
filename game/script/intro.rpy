default intro.axolotl_wakeupCount = 0
default intro.peeper_questions = []
default intro.peeper_flirted = False
default intro.frog_kneeled = False

label axolotl_intro:
    "Today, you are beginning your work in the amphibian kingdom. It’s been a long journey, but now it is time to work."
    "You’re awaiting your first audience with Queen Axolotl."

    "The guard calls you in."

    scene bg axolotl with dissolve

    "The throneroom is a lofty, well lit space. Arches made of marble are adorned with dangling glass pendants, holding up a ceiling built to look like a tranquil pond."
   
    "Seated on a throne, the queen seems to be deep in thought."
    "As you walk up, the sound of your boots striking the bare tiled floor echoes across the chamber. "

    show axolotl sleepy at right
    
    "Now at what feels to be the correct distance, you stand in front of her. 
    She’s wearing a simple white dress, but her gills are gilt with chains of pearl and glass ornamentation. "
    
    "She breathes softly, and mumbles underneath her breath. Her eyes are closed. She doesn’t stir."

    a "…taxes…"

    menu .axolotl_wakeup:
        "Um… hi?":
            pass
        "My Queen. <kneels>":
            pass
        "…":
            $ intro.axolotl_wakeupCount += 1
            if intro.axolotl_wakeupCount <= 2:
                a "*snore*"
                jump .axolotl_wakeup
            else:
                pass

    show axolotl happy

    "She startles."

    play music "music/macleod/Wallpaper.mp3"

    a "O-oh, um, sorry, I didn’t see you there!"

    "She hurriedly stands up, and quickly stamps down the dias her throne is elevated upon."

    show axolotl at default with move

    "She stumbles at the last step, sending her hurtling towards you."

    menu:

        "Offer her an arm to steady herself":
            "Before she falls further, she grabs your arm and steadies herself. You make eye contact. She looks tired."
            "Her eyes look irritated, there are discolourations underneath them, and her hand feels clammy and hot." 
            "She gives you a slight smile, then straightens up."

        "Step forward and catch her before she falls over":
            "You step forward, anticipating a fall. She stumbles for a bit, and loses her footing entirely."
            with vpunch
            "She falls into your awaiting arms, face-first. It’s not elegant." 
            "She’s light, and fragile. Her gills brush up against your back."

            menu:

                "Immediately set her straight":
                    "You set her back on her feet. She brushes herself off and takes a deep breath."

                "Hold onto her for a bit longer, and let her find her own feet":
                    "The moment feels like it lasts forever."
                    "She takes a couple breaths into your ear. You feel her relax a bit." 
                    "She then extricates herself from you and stands up straight."
                    show axolotl blush
                    "She’s blushing."

                "Discreetly pretend to lose your balance and fall down":
                    a "A-ah!"
                    hide axolotl with vpunch
                    "You both tumble into a heap. It's quiet for a bit. You both stay still." 
                    "Then you can feel her giggling into your shoulder."
                    show axolotl laugh
                    "Standing up, she laughs and laughs with her face in her hands." 
                    "You can't help but giggle too."
                    a "Heh. Hahaha. Alright, let's get to business then."


        "Stand aside and don’t put your hands on royalty":
            "She stumbles for a bit, leans forward, windmills her hands, and then eventually finds her footing."
            show axolotl sad
            "Is she pouting a bit…?"
    
    show axolotl happy

    a "*ahem*. Let’s try that again. Greetings, I am Queen Axolotl. It is a pleasure to make your acquaintance."

    menu:
        a "Tell me, what brings you to me on this fine day?"
        "I am the advisor you requested. I hear that you have troubles…?":
            pass
        "There was an ad for a 'consultant'. I was told that this was an interview…?":
            pass
        "Gosh, I’m not sure. I just walked in. Isn’t your security a little lax?":
            pass

    a "Oh, great! I really did need some help."
    
    a "There’s a lot of issues in my kingdom, but the kind of help I need most right now is a diplomat and ambassador." 

    a "I just can’t find the time to talk to all the other sovereigns."
    
    a "Baron Olm's ore exports are becoming lower quality and I need someone to check up on what's going on with that."

    a "Our trade deal with Herzog Frog's Anura Duchy is coming up and we need to renegotiate it."

    a "I can tell you more about the situation if you’d like before you choose one."
    
    menu:
        "Yes, I'd like to ask some questions.":
            call axolotl_info
        "I'll talk to Baron Olm.": 
            a "Great! Let's get you on your way..."
            jump olm_intro
        "I'll talk to Herzog Frog.":
            a "Great! Let's get you on your way..."
            jump frog_intro

label peeper_intro:
    scene bg castle_outside

    "You're packed into a caravan and taken to Herzog Frog's Duchy."
    #TODO: some scenery.

    "As you approach the gates to the castle, a booming voice echoes across the scenery."

    "Unknown" "{size=[text_size.larger]}Halt!{/size}"

    "You look around in surprise. What was that? You spot a small frog standing next to the gates. Surely it couldn't be?"

    show peeper at right with moveinbottom
    play music "music/macleod/Cipher2.mp3"

    p "I am Squire Spring Peeper, doorman of this castle!"

    "The frog peeps up at you. The squeaky, high-pitched voice was nothing like the voice before, but you have no choice but to conclude that they are the same source."

    menu:
        p "You have arrived at the abode of Herzog Frog, highest Frog in the realm! State your business!"

        "I am on official business from Queen Axolotl.":
            "The frog stares at you, incredulous."
            p "The Queen sent you...? We weren't told of any such visit."

        "I have a trade deal to offer the Herzog.":
            p "A trade deal...? Hmm..."
            p "I suppose that should be alright."

        "I am a long-lost relative of the Duke, here to reunite.":
            "The frog doesn't seem completely convinced."
            p "Well... okay..."
    
    menu: 
        p "I can take you into see His Grace, but I'll need to pat you down first. Is that okay?"
        "Yes, of course":
            pass
        "Fine.":
            pass
    
    "Peeper professionally pats your person for potentially powerful pikes, pistols, or pocketknives."
    "He finds nothing."

    p "Follow me closely, I'll escort you."

    hide peeper with moveoutright
    scene bg castle_inside
    show peeper at right
    with dissolve

    menu .peeper_questions:
        set intro.peeper_questions
        "While you're walking, it could be a good time to make some casual conversation, or to ask some questions."

        "How long have you been doing this job for?":
            "Peeper looks a bit unhappy."
            p "'Job'? This isn't just a job! This is my life's calling!"
            p "Herzog is one of my distant uncles, and when he put out a call for wards, my father sent me off from the cold frontier lands." 
            p "Since, I've been under his tutelage as a squire."
            p "It's been months, now. He's taught me everything I know."
            jump .peeper_questions

        "Was that you who yelled halt, or was it someone else? That scared me a bit.":
            "Peeper looks proud."
            p "Anura specialty! His Grace says that my croak is the second-best he's ever heard. After him, of course."
            p "That's part of why I became his herald and doorman. I can call the rest of the castle to attention if something goes wrong."
            menu:
                p "Hey, do you want me to do it again?"
                "Yes!":
                    p "{size=[text_size.larger]} Halt! {/size}"
                    p "Did you like it?"
                    "Peeper beams with pride."
                "No.":
                    p "Oh... okay..."
            jump .peeper_questions

        "Can you tell me a bit about Herzog Frog?":
            p "Well, first thing you should know is he's really good at leadership, chess, stand-up comedy, public speaking, administration, warfare, mock warfare, checkers, dueling, fencing, architecture, urban planning, hugging, telling when someone is lying, jumping, croaking, playing dead, knitting, cartography, singing, dancing, embroidery, art, wood carving, masonry, music, composition, calligraphy, tracking and hunting, cooking, swimming, holding his breath for a really long time, organization, gymnastics, yoga, meditation, philosophy"
            p "He likes being called His Grace, or Your Grace. You should try to stick to those."
            p "And he {i}loves{/i} being complimented. Just don't call him cute. He really hates that."
            jump .peeper_questions

        "Keep walking in silence." if len(intro.peeper_questions) <= 2:
            if len(intro.peeper_questions) == 1:
                "You walk in silence."
                "Peeper vibrates awkwardly, seeming to want to gush about something or someone."
                "He thinks better of it."
            else:
                pass
    
    show peeper at center with move

    "Peeper arrives at a door and knocks on it with this peculiar pattern."
    p "His Grace will be ready soon."
    "Peeper stands to attention. He seems nervous and jittery." 

    menu:
        "Thank you for escorting me.":
            p "No problem. It's what I'm here for."

        "I appreciated talking to you, it's really calmed my nerves." if len(intro.peeper_questions) >= 2:
            p "Of course! I'm always glad to tell someone of the brilliance of the great Duke Herzog!"

        "You know Spring Peeper, you're kind of a cutie yourself." if len(intro.peeper_questions) >= 3:
            $ intro.peeper_flirted = True
            "The squire blushes and stammers."
            p "u-um..."

        "Wait silently.":
            "A few awkward moments pass. Peeper looks straight ahead."

    "You hear a little bell from the room beyond him."

    if intro.peeper_flirted:
        p "uh, her Grave is ready{nw}"
        p "I-I mean, h-His Grace."
        p "His Grace is ready for you now."
        p "You can go."
    else:
        p "Oh, that means His Grace is ready. Go on in, don't keep him waiting."
    
    "Peeper opens the door for you and waves you in."

label frog_intro:
    scene bg frog
    show advax_frog_sword
    show advax_frog_throne
    show advax_frog
    with dissolve
    play music "music/macleod/Fluffing a Duck.mp3"
    f "..."
    jump .frog_greeting
    
    label .called_cute:
        f "...Ribbit."
        menu:
            f "Never call me that. Ever again. Ribbit."
            "What, cute? What's wrong with that?":
                f "I need not explain myself to a commoner. Ribbit."
            "Oh. I'm sorry your dukeyness.":
                f "As you should be. The correct form of address to a Duke is \"Your Grace\. Ribbit."
            "I duly apologise, Your Grace.":
                f "O-hoh! A commoner with manners! How intriguing. Ribbit."
        f "I will allow you to try again. Do keep in mind what I have told you. Ribbit."
        return
    
    menu .frog_greeting:
        "The Herzog sits on his chair, in silence. He watches you as you approach. He seems to want you to make the first move."
        "Stay standing":
            pass            
        "Bow":
            pass
        "Kneel":
            $ intro.frog_kneeled = True
        "Prostrate yourself":
            $ intro.frog_kneeled = True

    call sys_greeting
    "You" "{size=[_return.what_size]}[_return.string]{/size}"

    f "Sentiment: [_return.sentiment]"

    menu .frog_start:
        f "I am Herzog Frog. My power is unmatched. All those who dare to betray me will taste destruction. Ribbit."
        "Oh mighty leader, I am truly humbled.":
            f "You have recognized my mightyness and greatness. Good. Ribbit."
            f "Humility is a virtue most valuable in these realms. It will serve you well."
        "If you are as great as you claim, you will have no problem besting me in a battle of wits.":
            menu .tell_joke:
                f "Oh, is that so? I accept! I have more wit than any other amphibian. I'll start. Knock knock. Ribbit."
                "Who's there?":
                    menu:
                        f "Frog. Ribbit."
                        "Frog who?":
                            f "I frog-ot to tell you I'm a prince in waiting. Haha. Ribbit."
                        "Frog ribbit who?":
                            f "Frog going to ribbit you to shreds soon. Ribbit."
                        "Eh, froggettabout it.":
                            f "...Ribbit."
                "Knock knock. Aha, who has the upper hand now?":
                    "Blah"
                "The cute frog's telling knock knock jokes! Dad, get the camera. This needs to go viral.":
                    call .called_cute
                    jump .tell_joke
        "A tiny frog with a giant sword! It's so cute!":
            call .called_cute
            jump .frog_start
    
    $ print("blah")
    jump .import_taxes


    label .import_taxes:
        f "Now tell me, for what have you come here for?"
        play music "music/macleod/On the Ground.mp3"
        f "You say that the trade deal is up for renegociation?"
        f "I'll be the judge of that."
        f "..."
        f "..."
        f "..."
        "The Frog appears to be deep in thought."
        f "..."
        f "..."
        f "..."
        f "..."
        f "Ambassador of the Axolotl."
        f "It is a good tiding that you are here today, for I was about to send a representative to re-negociate the trade deal between the Kingdom of Ambystoma and the Anura Duchy."
        menu:
            f "As the host, I would like to offer you the chance to make the first offer."
            "Total free trade agreement.":
                f "No, absolutely not."
            "Same agreement as last time.":
                f "Perhaps."
            "We will reduce the import tax on fruitflies and beetle larvae by 4\% for a commensurate decrease in the sale of Axolotl-branded merchandise in your country towns.":
                f "Perhaps."
            "No, you first.":
                f "Okay."
        menu:
            f "I am raising import tax by 4\%. Ribbit."
            "But Queen Axolotl cannot accept that!":
                "blah"
            "Well, I'm raising import tax by 5\% then. Let's see who wins this trade war.":
                "blah"
            "Is that a speech impediment or do all frogs just say ribbit at the end of every line?":
                "blah"

label olm_intro:
    scene bg olm
    show advax_olm_body
    show advax_olm_head
    menu:
        o "That is not acceptable. Try harder."
        "Will you accept my deal?":
            o "You are dreaming. Please wake up."
        "Screw you, you blind worm.":
            "blah"
        "I give up.":
            "blah"