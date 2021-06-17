import requests
import tokenz
from pprint import pprint



post_message_url = 'https://slack.com/api/chat.postMessage'



channel_id = 'C0252M0SSP6'


def squawk(text_to_send):
    message_content =[('token', tokenz.bot_oath_token), ('channel', channel_id), ('text', text_to_send)]
    response = requests.post(url = post_message_url,data = message_content)


