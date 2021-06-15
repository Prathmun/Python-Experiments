import requests

test_url = 'https://slack.com/api/api.test'

post_message_url = 'https://slack.com/api/chat.postMessage'

bot_oath_token = 'xoxb-2159771144566-2163476870501-6GlFIlBxNLosg88nBita14ez'

channel_id = 'C0252M0SSP6'

message_content =[('token', bot_oath_token), ('channel', channel_id), ('text', "Hello World")]
def greeting()
    response = requests.post(url = post_message_url,data = message_content)



#for each in response.iter_lines():
 #   print(each)


