default greeting.set = []
default greeting.string = " "
default greeting.allcaps = False
default greeting.what_size = text_size.normal
default greeting.sentiment.pos = 0
default greeting.sentiment.neg = 0

label sys_greeting:
    jump .greetingStart

    label .construct_greeting_string:
        python:
            greeting.string = ' '.join(greeting.set)
            if greeting.allcaps == True:
                greeting.string = greeting.string.upper()
            else:
                greeting.string = greeting.string[:1].upper() + greeting.string[1:]
        return

    label .change_sentiment(delta=0):
        python:
            if delta < 0:
                #checks for negative; reverses.
                greeting.sentiment.neg -= delta
            if delta > 0:
                greeting.sentiment.pos += delta
        return

    label .greetingStart:
        $ greeting.set = []
        call .construct_greeting_string

    menu:
        set greeting.set
        "[greeting.string]"
        "hey,":
            pass
        "hello,":
            pass
        "greetings,":
            call .change_sentiment(1)
        "dear,":
            call .change_sentiment(1)
        ",":
            pass

    menu:
        set greeting.set
        "[greeting.string]"
        "my":
            call .change_sentiment(1)
        "you":
            pass
        "our":
            pass
        "...":
            $ greeting.set.pop()

    menu:
        set greeting.set
        "[greeting.string]"
        "handsome":
            call .change_sentiment(1)
        "powerful":
            call .change_sentiment(1)
        "cute":
            call .change_sentiment(-1)
        "prodigal":
            call .change_sentiment(-1)
        "...":
            $ greeting.set.pop()

    menu .noun:
        set greeting.set
        "[greeting.string]"
        "Prince Frog":
            call .change_sentiment(1)
        "Duke Frog":
            call .change_sentiment(1)
        "Herzog Frog":
            call .change_sentiment(1)
        "Frog":
            call .change_sentiment(-1)
        "...":
            $ greeting.set.pop()

    menu:
        set greeting.set
        "[greeting.string]"
        ", your mother smells of hamsters and your father smells of elderberries":
            call .change_sentiment(-1)
        ", your greatness is well reknowned, and I came to see it for myself":
            call .change_sentiment(1)
        ", your squire is well trained and is the very image of you. I applaud it":
            call .change_sentiment(1)
        ", your tracts of land are enormous and well trimmed":
            call .change_sentiment(1)

    menu:
        "How loud do you want to say it?"
        "Yell it":
            $ greeting.what_size = text_size.large
            $ greeting.allcaps = True
        "Loud":
            $ greeting.what_size = text_size.large
        "Normal":
            pass
        "Quiet":
            $ greeting.what_size = text_size.small
            call .change_sentiment(-1)

    call .construct_greeting_string

    "Your sentence is:"
    menu:
        "{size=[greeting.what_size]}[greeting.string]{/size}"
        "Say it!":
            return greeting
        "Go back to the beginning":
            jump sys_greeting