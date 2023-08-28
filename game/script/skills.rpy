init python:
    import collections

    StateChange = collections.namedtuple('statechange', ['prop', 'delta'])

    class GameCharacter:
        def __init__(self, name, description):
            self.name = name
            self.description = description
            self.attributes = {}
            self.skills = {'body': Skill('body', 'body'), 'mind': Skill('mind', 'mind')}
        def update_skill(self, change_tuple, shouldNotify = True):
            notification = []
            for i in change_tuple:
                skill_name = i[0]
                change = i[1]
                self.skills[skill_name].number += change
                notification.append(f"{change:+} {skill_name}")
            renpy.notify(", ".join(notification))

    class Skill:
        def __init__(self, name, description):
            self.name = name
            self.description = description
            self.number = 0
    
    player = GameCharacter("player", "the player character.")

# # Attributes
# default player.body = 0
# default player.heart = 0
# default player.brain = 0

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