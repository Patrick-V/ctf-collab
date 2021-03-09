from env import config
import requests

am_email = 'mneiding@cisco.com'
se_email = 'frewagne@cisco.com'

headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}",
    'Accept': 'application/json',
}

def create_space(space_title):
    '''
    Creates space and returns its' ID
    '''
    payload = {'title': space_title}
    response = requests.post(f"{config['WEBEX_BASE_URL']}/v1/rooms", headers = headers, data = payload)

    if response.status_code == 200:
        space_id = response.json()['id']
        print(f"{space_title} was succesfully created!")
        return space_id
    else:
        print("Unsuccesful in creating space")
        return None

def add_to_space(space_id, person_email):
    payload = {
            'roomId': space_id,
            'personEmail': person_email,
        }

    response = requests.post(f"{config['WEBEX_BASE_URL']}/v1/memberships", headers = headers, data = payload)
    if response.status_code == 200:
        print(f"{person_email} was succesfully added to the space")
    else:
        print(f"{person_email} could not be added to the space")
        return None

def send_welcome_everyone(space_id):
    payload = {
        'roomId': space_id,
        'files': 'https://media.giphy.com/media/XD9o33QG9BoMis7iM4/giphy.gif'
    }
    response = requests.post(f"{config['WEBEX_BASE_URL']}/v1/messages", headers = headers, data = payload)

    if response.status_code == 200:
        print(f"Everyone was welcomed")
    else:
        print(f"Welcome was unsuccesful")
        return None

if __name__ == '__main__':
    space_id = create_space('This message was made possible by Squarespace')

    add_to_space(space_id, am_email)
    add_to_space(space_id, se_email)

    send_welcome_everyone(space_id)