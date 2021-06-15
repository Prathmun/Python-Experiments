from faerie_story import scene_list
from slack_bot_squawker import squawk

def story_teller(scene, selection):
    if selection == 'start':
        squawk(scene_list["faerie_ring"])
        return scene_list["faerie_ring"]

    (print(selection) for i in range(1,1000))
    
    scene_looker = scene_list['faerie_feast']
    
    
    squawk(str(scene_looker))
    return_scene = scene.paths[0]
    return scene_list[return_scene]

