label axolotl_intro:
    default flag_intro_olmFirst = False
    default __axolotl_wakeupCount = 0
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

    nvl clear

    a "…taxes…"

    menu .axolotl_wakeup:
        "Um… hi?":
            pass
        "My Queen. <kneels>":
            pass
        "…":
            $ __axolotl_wakeupCount += 1
            if __axolotl_wakeupCount <= 2:
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

    a "You're hired. You start tomorrow."

    a "There’s a lot of issues in my kingdom, but the kind of help I need most right now is a diplomat and ambassador."

    a "I just can’t find the time to properly talk to all the other sovereigns."
    
    a "Your first job will be to introduce yourself to our closest trading partners: Herzog Frog and Baron Olm."

    a "Meet me back here tomorrow and I'll give you the details. For now, get some rest. I'll have the servants prepare quarters for you and get you acquainted with the complex."

    scene bg black

    #TODO: Write a servant character?

    "You're whisked away by a servant and given a tour of the complex."

    "There are a couple amenities in the complex that you might be interested in. Would you like to spend some time getting used to them?"

    menu:
        "What would you like to do?"
        "Go to the library and read something":
            "You read something."
        "Practise archery":
            "You practise archery."
        "Just wander around":
            "You wander around."

    "After spending the rest of your day exploring the complex, you're tired out. You go to sleep."

    scene bg axolotl

    a "Good morning! I hope you slept well."

    a "As we spoke yesterday, I'll have you introduce yourself to either Baron Olm or Herzog Frog."

    menu:
        a "Which do you want to meet today?"
        "Herzog Frog":
            pass
        "Baron Olm":
            $ flag_intro_olmFirst = True    

    a "Oh, and before you go,"

    "Queen Axolotl rummages in a nearby drawer."

    a "Here. Your badge of station."

    "Queen Axolotl presents a signet ring, with the seal of the Kingdom of Ambystoma printed on it. As you accept it, it's weighty and cold."

    call .ring_wearing

    a "Make a good first impression! You'll be my representative. It's an important job, and I need you to do it well."

    if flag_intro_olmFirst:
        jump olm_intro
    else:
        jump frog_intro

    menu .ring_wearing:
        "How do you wear it?"
        "My left hand.":
            call .finger_choice
        "My right hand.":
            call .finger_choice
        "Around my neck, on a string or necklace.":
            pass
        "I'll just keep it in my pocket until I need it.":
            pass
    return

    menu .finger_choice:
        "Which finger?"
        "Pinky":
            pass
        "Ring":
            pass
        "Middle":
            pass
        "Index":
            pass
        "Thumb":
            pass
    return

label frog_intro:
    default __peeper_questions = []
    default __peeper_flirted = False

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
    
    p "I can take you into see His Grace, but I'll need to pat you down first."
    
    "Peeper professionally pats your person for potentially powerful pikes, pistols, or pocketknives."
    "He finds nothing."

    p "Follow me closely, I'll escort you."

    hide peeper with moveoutright
    scene bg frog
    show peeper at right
    with dissolve

    menu .peeper_questions:
        set __peeper_questions
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

        "Keep walking in silence." if len(__peeper_questions) <= 2:
            if len(__peeper_questions) == 1:
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

        "I appreciated talking to you, it's really calmed my nerves." if len(__peeper_questions) >= 2:
            p "Of course! I'm always glad to tell someone of the brilliance of the great Duke Herzog!"

        "You know Spring Peeper, you're kind of a cutie yourself." if len(__peeper_questions) >= 3:
            $ __peeper_flirted = True
            "The squire blushes and stammers."
            p "u-um..."

        "Wait silently.":
            "A few awkward moments pass. Peeper looks straight ahead."

    "You hear a little bell from the room beyond him."

    if __peeper_flirted:
        p "uh, his Grav-{nw}"
        p "I-I mean, h-His Grace."
        p "His Grace is ready for you now."
        p "You can go."
    else:
        p "Oh, that means His Grace is ready. Go on in, don't keep him waiting."
    
    "Peeper opens the door for you and waves you in."

    jump .frog_intro
    
    default __frog_kneeled = False
    
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
        
    menu .joke_response:
        "Laugh loudly and for a long time. Feign that you can't breathe and fall upon the floor":
            "blah"
        "Giggle.":
            "blah"
        "Loudly exhale through your nose.":
            "blah"
        "Stay stone-silent.":
            "blah"

    f "yes... yes, good. Now it is your turn. Ribbit."
    menu:
        "What kind of joke would you like to tell?"
        "A long winded shaggy dog story":
            "So, there's a man crawling through the desert."
            show bg frog with fade
            "...Wait! The sun was setting! That meant he was going to have to spend another night out here! Arrrgh!"
            show bg frog with fade
            "Wow, 167 years. That's almost 140 more years I'll live if I live as long. Do you know what he died of, Nate?"
            show bg frog with fade
            "\"Better Nate than lever!\", he ran over the snake."
        "Observational humour on a personal experience":
            pass
        "A pithy piece of punnage":
            pass
        "Tell the frog that you can't live up to his standards":
            pass

    label .frog_intro:
        scene bg frog
        show frog
        with dissolve
        play music "music/macleod/Fluffing a Duck.mp3"
        f "..."

        menu:
            "The Herzog sits on his chair, in silence. He watches you as you approach. He seems to want you to make the first move."
            "Stay standing":
                pass            
            "Bow":
                pass
            "Kneel":
                $ __frog_kneeled = True
            "Prostrate yourself":
                $ __frog_kneeled = True

        call sys_greeting
        "You" "{size=[_return.what_size]}[_return.string]{/size}"

        f "Sentiment: [_return.sentiment.pog - _return.sentiment.neg]"

        menu:
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
                                call .joke_response
                            "Frog ribbit who?":
                                f "I frog-ot to tell you I'm a prince in waiting. Haha. Ribbit."
                                call .joke_response
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
    
    label .archery_challenge:
        menu:
            f "How about a bout of archery?"
            "Yes, absolutely.":
                pass
            "No thank you.":
                pass
        
        "Surprisingly, Herzog Frog is quite good at archery."
        "Using his hind legs, there is some measure of power and grace."
        f "Your technique is interesting. I've never quite seen anyone use a bow like that. Ribbit."
        menu:
            "I could say the same for you.":
                f "I've developed this technique myself. I can confidently say that I'm the best archer ever. Ribbit."
            "Thank you.":
                pass
            "Are you being condcending?":
                pass
        "You're neck to neck. Herzog Frog lands a shot that pulls him ahead of you."
        menu:
            "You can only win with a bullseye."
            "Try for the win":
                pass
            "Go for a low scoring shot that you definitely can hit.":
                pass
    
    label .chess_challenge:
        menu:
            "You're playing black. You recognize the Duke's opening as open to a Fool's Mate."
            "Take advantage and win the first game":
                pass
            "Ignore it and play normally":
                pass
        
        menu:
            "It's a rematch. You're playing white. What's your playstyle?"
            "Early queen pressure. He'll fold.":
                "You bring your queen out within the first three moves."
                "Herzog Frog sees through your scholar's mate, and calmly closes up his position."
                "You get to the middle game without any material advantage, but Herzog Frog's position is practically impenetrable."
            "A closed, stable position, then apply slow pressure.":
                "You play - and Herzog Frog appears irritated."
            "The bongcloud. The king should lead from the front.":
                "You lose."

    if flag_intro_olmFirst:
        jump sys_travel

label olm_intro:
    scene bg olm
    label .newt_intro:
        "The Queen gives you directions to the OIm's home. It's quite a distance away from anything else."

        "Eventually you arrive at what you think is the right spot. There's absolutely nothing around, though."

        show newt

        n "You there! I haven't seen you around before. How do you do?"

        n "Anyway, now with pleasantries out of the way, you look like the sort of chap  that looks like they want to see Baron Olm. Would that be right?"

        #TODO: replace "chap" with something gender-neutral

        n "I thought so. Well, come along with me now, I'll get you there in one piece."

        "Countess Newt tromps through the swamp, eventually reaching a pier with a small rowboat."

        "Newt gets into the front of the boat."

        n "Hop to it now! I haven't got all day! I'll navigate, you drive."

        n "I found this rowboat, and have just been looking around for someone to row it! Now you've come along, so you're a perfect fit."

        "Newt navigates through the mangrove and into a cave. At the end of the long tunnel, you reach a dry landing, with a built stone wall and a solid wooden door."

        "Newt disembarks and knocks on the door."

        n "Hello? Olmyy!"

        n "No response. No problem, I have a spare key."

        "Newt opens the door."

        n "Come, come, warm yourself in the living room. Olm isn't the biggest one for niceties, but I absolutely *insisted* that he install a fireplace. Firewood's over there, here's a poker. Enjoy!"

        "Before you get the chance to interrupt, Newt practically flies across the room. She knocks on another door, and opens it. Just before entering, she turns back to you:"

        n "I'll be quick, Darl. I'll let Olm know you're waiting."
        hide newt

        "Newt exits the chamber, and waves you in."

        "It's dark. Your eyes adjust to the cave."
        
        show olm

        o "Hello."

        o "Now, why is an outsider to the kingdom inside my innermost chamber...?"

        o "Yes, yes. Newt let you in. I don't know why she did that. But please, make it quick. I have many more important things to tend to than... whatever this is."

        "Olm gestures in your general direction."
    
    if flag_intro_olmFirst:
        jump sys_travel
    else:
        jump frog_intro