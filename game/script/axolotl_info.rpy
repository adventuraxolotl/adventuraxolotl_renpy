label axolotl_info:
    menu:
        "Amphibian Kingdom":
            a """
            The Amphibian Kingdom is well... not a kingdom. Technically we're a class. 

            De Jure, we're a federal electoral monarchy, with Sovereigns who collaboratively govern the realm via the Great Council.

            The elected monarch is more of a ceremonial position than anything else. 
            
            Technically they control the federated armies and fleets during wartime, but really those are their own thing.

            Since my grandmother's rule, the Axolotl Kingdom has been the real power, bypassing the Great Council entirely. 
            
            Many of the other Sovereigns have pledged alligeance to us, and are dependent on us for protection and trade.
            """
            label .kingdomQuestions:
                menu:
                    "What happened to the Great Council?":
                        a "Since then, the Great Council has been kind of been taken over by old religiously fanatic toads."
                        a "They make proclamations now and then but nobody really listens."
                        a "It's still good to pay lip service to the Great Council though. They just weird me out."
                        jump .kingdomQuestions
                    "Grandmother?":
                        a "My grandmother was a visionary architect and urban designer. She designed this hall and planned our cities." 
                        a "When she took the throne, she developed a key relationship with the captains of industry."
                        a "It ensured that our cities are the heartland of the Kingdom's economy. Since then, our advantage has only grown."
                        jump .kingdomQuestions
                    "Armies and Fleets?":
                        a "The Federal Army and the Federal Fleet are technically under my control, but they have a strong loyalty to the stability of the Kingdom."
                        a "Their recruits come from all over the Amphibian Kingdom, but consist mostly of Frogs and Toads."
                        a "Commander Salamander heads the Army, and Captain Cicilian heads the Fleet. They butt heads from time to time, but work together well."
                        jump .kingdomQuestions
                    "No more questions":
                        jump axolotl_info
        "Queen Axolotl?":
            a "Oh, me? I guess I can tell you a bit about myself."

            a "I'm the latest and greatest in a long long line of axolotl monarchs."
            
            a "My mother went missing, so I've had to take over running the kingdom." 
            label .axolotlQuestions:
                menu:
                    a "Was there anything specific you wanted to know about?"
                    "Strengths?":
                        a "Well, the kingdom is the best managed land around. We have the highest population density cities, a strong industry, and a booming economy."
                        jump .axolotlQuestions
                    "Difficulties?":
                        a "I just don't feel like anyone respects me. It's been a hassle trying to get everything running again."
                        jump .axolotlQuestions
                    "Opportunities?":
                        a "Gosh, I couldn't think of anything like that. Everything's been way too hectic."
                        jump .axolotlQuestions
                    "Threats?":
                        "The Queen makes sure that nobody else is in the chamber, and comes closer to you."
                        "She whispers in your ear:"
                        a "{i}Everything.{/i}"
                        a "I'm afraid that the other Sovereigns are out to improve their lot with my mother gone." 
                        a "She was the peacebroker, and now I'm here instead. I wasn't built for this."
                        jump .axolotlQuestions
                    "Ask about something else":
                        jump axolotl_info
        "Baron Olm?":
            a """
            Baron Olm is... difficult. He's a recluse and lives in a damp cave. 

            Literally. 

            The rest of the Amphibians at least get some sunlight now and then, but I've never seen the Baron at any function.

            I don't think he likes me very much. 
            """
            label .olmQuestions:
                menu:
                    a "Anything else about the Baron?"
                    "Burghers?":
                        a "Yeah, you know. Barons of Industry. They make steel and stuff. It's what our kingdom is built upon."
                        jump .olmQuestions
                    "What does he like?":
                        a "Well... I don't actually know all that much about the Baron myself. I know that he holes himself up in his... hole... and tinkers with technology. I can't understand it myself."
                        jump .olmQuestions
                    "Done with questions":
                        jump axolotl_info
        "Herzog Frog?":
            a "Herzog Frog is... charming?"
            jump axolotl_info
        "Done with questions":
            return