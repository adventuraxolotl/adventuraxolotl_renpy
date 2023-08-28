init python:
    import collections
    from enum import Enum

    class GameCharacter:
        def __init__(self, name, description):
            self.name = name
            self.description = description
            self.skills = collections.Counter()
            self.testskills = {'body': 0, 'mind': 0, 'heart': 0}
        def update_skill(self, change_tuple, shouldNotify = True):
            notification = []
            for i in change_tuple:
                skill_name = i[0].value
                change = i[1]
                self.testskills[skill_name] += change
                notification.append(f"{change:+} {game_skills[skill_name].name}")
            if shouldNotify:
                renpy.notify(", ".join(notification))

    class SkillProperties:
        def __init__(self, name, description):
            self.name = name
            self.description = description
    
    class SKILL(Enum):
        BODY = 'body'
        MIND = 'mind'
        HEART = 'heart'

    game_skills = {
        SKILL.BODY: SkillProperties('body', 'body'), 
        SKILL.MIND: SkillProperties('mind', 'mind'),
        SKILL.HEART: SkillProperties('heart', 'heart')
        }

default player = GameCharacter("player", "the player character.")

screen skill_panel:
    frame:
        has vbox
        for i in game_skills:
            hbox:
                text "[i.value]:"
                bar value player.testskills[i.value] range 100
# #Skills
# default player.warfare = 0
# default player.dexterity = 0
# default player.hardiness = 0

# default player.persuasion = 0
# default player.empathy = 0
# default player.bluff = 0

# default player.technical = 0
# default player.admin = 0
# default player.politics = 0