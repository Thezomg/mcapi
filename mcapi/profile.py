## Based on Java from https://github.com/Mojang/AccountsClient/

import requests
import json

AGENT = "minecraft"
PROFILE_URL = "https://api.mojang.com/profiles/page/{page}"
UUID_PROFILE_URL = 'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}'

class ProfileCriteria(dict):
    def __init__(self, name, agent):
        self['name'] = name
        self['agent'] = agent

def get_profile(uuid):
    url = UUID_PROFILE_URL.format(uuid=uuid)
    try:
        r = requests.get(url)
        profile = r.json()
    except:
        profile = None

    return profile

def get_uuid(*name):
    if len(name) == 0:
        return None
    crit = [ProfileCriteria(x, AGENT) for x in name]
    p = []

    page = 1
    while True:
        url = PROFILE_URL.format(page=page)
        data = json.dumps(crit)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        r = requests.post(url, data=data, headers=headers)
        profiles = r.json()
        if 'profiles' in profiles:
            if profiles['size'] == 0:
                break
            p.extend(profiles['profiles'])

        page += 1
                
    return p
