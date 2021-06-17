import pprint as pp
import json
import os
from flask import Flask, request, Response
from story_teller import story_teller
import faerie_story
from tokenz import SLACK_WEBHOOK_SECRET
app = Flask(__name__)




@app.route('/slack', methods=['POST', 'GET'], )
def inbound():
    print("was hit")
    
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200

#.\ngrok.exe http 5000 
# use this to forward the listening port
current_scene = faerie_story.faerie_ring

@app.route('/', methods=['GET','POST'])
def test():
    global current_scene
    content = request.get_json()
    #(print(content['event']['text']) for i in range(1, 100))
    #print(int(content['event']['text']))
    #print(type(content))
   # print(content.keys())
    #python_from_json = json.load(content)
    
    if 'challenge' in content.keys():
        #challenge = request.form.get('challenge')
        return Response(content['challenge']), 200
    #(print(type(content['event']['text'])) for i in range(1,1000))
    #(print(content['event']['text']) for i in range(1,1000))
#if content['event']['text'] == 'start':
        #set scene to faerie_ring
    if content['event']['text'] == 'start':
        current_scene = story_teller(current_scene, 'start')
    if content['event']['text'].isnumeric() == True:
        current_scene = story_teller(current_scene, content['event']['text'])
    else:
        #pp.pprint(content)
        pass    
    return ""



if __name__ == "__main__":
    app.run(debug=True)