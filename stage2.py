# Query and send to a space
#TODO Find the number of messages you have send per space you are in
#TODO Find the number of spaces you are in
#TODO Share those information as formatted text into a webex space.
from env import config
import requests
import stage0

def get_amount_scheduled_meetings():
    headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}",
    'Content-Type': 'application/json',
    }
    response = requests.get(f"{config['WEBEX_BASE_URL']}/v1/meetings?state=scheduled", headers = headers)
    if response.status_code == 200:
        return len(response.json()['items'])
    else:
        return None

def get_amount_messages_sent_per_space():
    list_spaces = get_list_rooms(True)
    list_space_ids = []
    for space in list_spaces:
        list_space_ids.append(space['id'])
    


def get_amount_joined_spaces():
    headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}",
    'Content-Type': 'application/json',
    }
    response = requests.get(f"{config['WEBEX_BASE_URL']}/v1/memberships?max=1000", headers = headers)
    if response.status_code == 200:
        return len(response.json()['items'])
    else:
        return None

def post_message(amount_scheduled_meetings, amount_joined_spaces, amount_messages_sent_per_space):
    headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}",
    'Accept': 'application/json',
    }
    payload = {
        'roomId': config['Y2lzY29zcGFyazovL3VzL1JPT00vM2ZmOGU3ZjAtODAwOS0xMWViLTg4NjUtNTE2OGI4NmU0NjA4']
        'markdown': f"I sent **{str(amount_messages_sent_per_space)}** messages per space, have **{amount_scheduled_meetings}** scheduled meetings and have joined **{amount_joined_spaces}** spaces!"
    }

    response = requests.post(f"{config['WEBEX_BASE_URL']}/v1/messages", headers = headers, data = payload)

    if response.status_code == 200:
        print(f"Everyone was informed")
    else:
        print(f"Informing was unsuccesful")
        return None

if __name__ == '__main__':
    amount_scheduled_meetings = get_amount_scheduled_meetings()
    amount_joined_spaces = get_amount_joined_spaces()


