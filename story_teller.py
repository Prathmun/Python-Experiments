from faerie_story import scene_list
from slack_bot_squawker import squawk

def story_teller(scene, selection):
    if selection == 'start':
        squawk(scene_list["faerie_ring"])
        return scene_list["faerie_ring"]
    
    
    squawk(scene_list[scene.paths[0][int(selection)-1]])
    return scene_list[scene.paths[0][int(selection)-1]]

