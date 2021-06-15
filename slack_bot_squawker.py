import requests



post_message_url = 'https://slack.com/api/chat.postMessage'

bot_oath_token = 'xoxb-2159771144566-2163476870501-6GlFIlBxNLosg88nBita14ez'

channel_id = 'C0252M0SSP6'


def squawk(text_to_send):
    message_content =[('token', bot_oath_token), ('channel', channel_id), ('text', text_to_send)]
    response = requests.post(url = post_message_url,data = message_content)



