
class Scene:
    def __init__(self, name, copy, paths,):
        self.name = name,
        self.copy = copy,
        self.paths = paths,

    def __str__(self,):
        return self.copy[0]


faerie_ring = Scene("Faerie Ring",
"""You've been lost in the forest for a long time. You stumble into a clearing, with a ring of large red spckeled mushrooms in the center, a Faerie ring. You can hear the soft clatter of plates, 
and the murmering of a distant crowd. You've heard of these before. You know that if you step into the ring, everything could change. Do you:

1. Step into the musical ring of mushrooms
2. Choose to test your luck with the seemingly endless forest """,
["faerie_feast", 'forest_wander']
)

forest_wander = Scene("Forest Wander",
""" You're no fool, you remember the stories about the Fae. You know no matter how lost you are, it can't be worse than the pernicious tricks of the Fae! You set off into the forboding woods at a brisk pace, confident
in your choice to forgoe the faerie diversion. Eventually your enthusaism wanes as the forest remains as dense and dark, despite the distance you've traveled. It's been days since you've eaten now, your feet hurt, you're starting to see things.
Deep in the woods, off from the path you've been following you see dancing blue lights. Do you
1. Follow the blue glowing lights
2. Stick to the path """,
['forest_escape', 'forest_path_death'])

faerie_feast = Scene("Faerie Feast",
"""You've been wandering in the forest for days now. You figure you're so lost that a meeting the Fae couldn't get you any more lost and you've always wanted to meet a Faerie. So you stride confidently into the center of the ring.
As your foot strikes the center of the ring, the clearing is suddenly full of brightly dressed revelars! There's a lively band, a buffet table that would put any cornocopea to shame, and casks and casks of wine. The trees are all illuminated by dancing blue lights.
 A beautiful woman, 
easily three feet taller than you, dressed in a flowing green dress approaches you. She smiles invitingly at you. She shouts joyfully 'Welcome to our party, we do not get many mortals!' She grins predatorally. 'Please stay and partake in our hospitality!"
Do you:
1. Take her offer to mean food, and descend upon the buffet
2. Step out onto the dance floor
3. Turn and run into the forest and the lights""",
[ "faerie_servant","dance_death", "forest_secape"])

forest_escape = Scene("",
"""Against you're better judgement you plunge into the undergrowth after the blue lights. As you set off towards them the sounds of bells fill your ears. As you stumble through the underbrush, the lights begin to dance faster and faster. 
Though the conditions worsen and your pace crawls to a literal crawl, the lights seme to be approaching you faster and faster. Soon they surrond you and are whirring around you with terrible speed. The bellsong has accelerated to match their
awful whirling. Faster and faster! As your vision is toally enveloped in whirling blue lights the storm of lights and sounds ceases. You are in a medow. You recognize this medow, you are close to home! You set off at a run, vowing never to enter 
the encahnted forest again """,
[])

forest_path_death = Scene("",
""" Ever confident in your distrust of strange beings in the forsest you stick to the path, truding determendly forward. You march and you march, but the forest never relents, always there is another tree, always this oppressive silence.
Shouldn't a forest at least have birdsong, the buzzing of insects? These are the questions you find yourself pondering when you finally collapse from exhaustion, no idea if you've even been moving. The forest becomes your final resting place. """,
[])

dance_death = Scene("Dance Death",
"""You've never heard music so lively, so sweet, so quick! The fae woman's invitation is all you need to skip out to the dance floor and join in on the revelry! The musicians quickly notice your passion for the music, and begin playing faster
Disinterested in resisting you speed up your dance to keep up. The musicains delighted, speed up in turn. They keep speeding up, and so do you. Soon you wish to stop, but the music keeps speeding up, and so do you.
Fast and faster you go, until eventually your face plastered with a manic grin you fall to the ground lifeless. The Fae music has caused you to dance youself to death. """,
[])

faerie_servant = Scene("faerie_servant",
"""The Faerie woman's offer is too generous to pass up! You descend up on the buffet, but not before pouring yourself a generous tankard of wine. You load up your plate and take a big gulp of the wine. It's elderberry wine,
but not like any you've had before. The wine is so rich it sets you to laughing. When your giggle fit finally subsides you relize the Fae woman had been laughing with you. She now locks eyes with you, her eyes 
kaelaediscopes of shifting color. She intones in a deep otherworldy voice 'Though hath partaken of the eternal revelers victuals! Thy shalt forever serve the never ending feast!' As she speaks you know that she speaks the truth
, you are now bound for all eternity to this feast. Oh well, at least the food is good """,
[])

scene_list = {"faerie_ring" : faerie_ring, "forest_wander" : forest_wander, "faerie_feast" : faerie_feast,  'forest_path_death' :forest_path_death, 'forest_escape' :forest_escape, 'dance_death' :dance_death, 'faerie_servant' : faerie_servant}



