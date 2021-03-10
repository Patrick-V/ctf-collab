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
    headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}",
    'Content-Type': 'application/json',
    }

    list_spaces = stage0.get_list_rooms()
    list_space_ids = []

    for space in list_spaces:
        list_space_ids.append(space['id'])
    
    list_amount_messages_sent_per_space = []
    for space_id in list_space_ids:
        message_counter = 0

        response = requests.get(f"{config['WEBEX_BASE_URL']}/v1/messages?roomId={space_id}", headers = headers)
        response_dict = response.json()['items']
        if response.status_code == 200:
            for message in response_dict:
                if message['personEmail'] == 'pverhage@cisco.com':
                    message_counter += 1

            list_amount_messages_sent_per_space.append(message_counter)
        else:
            print('Response failed!')
            return None
    
    return list_amount_messages_sent_per_space # out of every 50 last messages sent in a space
    
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
        'roomId': config['PRODUCTION_ROOM'],
        'markdown': f"I sent **{amount_messages_sent_per_space}** messages (out of the last 50 messages) per space, have **{amount_scheduled_meetings}** scheduled meetings and have joined **{amount_joined_spaces}** spaces!"
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
    amount_messages_sent_per_space = get_amount_messages_sent_per_space()
    post_message(amount_scheduled_meetings, amount_joined_spaces, amount_messages_sent_per_space)