import requests

test_url = 'https://slack.com/api/api.test'

post_message_url = 'https://slack.com/api/chat.postMessage'

bot_oath_token = '***'

channel_id = 'C0252M0SSP6'

message_content =[('token', bot_oath_token), ('channel', channel_id), ('text', "Hello World")]
def greeting()
    response = requests.post(url = post_message_url,data = message_content)



#for each in response.iter_lines():
 #   print(each)


