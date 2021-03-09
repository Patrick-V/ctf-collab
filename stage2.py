# Query and send to a space
#TODO Find the number of messages you have send per space you are in
#TODO Find the number of spaces you are in
#TODO Share those information as formatted text into a webex space.
from env import config
import requests

def get_amount_scheduled_meetings():
    headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}",
    'Content-Type': 'application/json',
    'state': 'scheduled'
}
    response = requests.get(f"{config['WEBEX_BASE_URL']}/v1/meetings", headers = headers)
    if response.status_code == 200:
        return len(response.json()['items'])
    else:
        return None


if __name__ == '__main__':
    amount_scheduled_meetings = get_amount_scheduled_meetings()


