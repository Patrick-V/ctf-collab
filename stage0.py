from env import config
import requests

space_name = 'CSAP Programmability CTF - Team 2'

def get_list_rooms():
    headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}",
    'Content-Type': 'application/json',
}

    response = requests.get(f"{config['WEBEX_BASE_URL']}/v1/rooms?max=999", headers = headers)

    if response.status_code == 200:
        list_rooms = response.json()['items']
        return list_rooms
    else:
        return None

def get_room_id(space_name):
    headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}",
    'Content-Type': 'application/json',
}

    list_rooms = get_list_rooms()

    if list_rooms == None:
        return None
    else:
        for room in list_rooms:
            if room['title'] == space_name:
                space_id = room['id']
        
        return space_id

if __name__ == '__main__':
    space_id = get_room_id(space_name)
    print(f"{space_id} is the ID belonging to space {space_name}")