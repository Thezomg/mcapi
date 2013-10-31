## Based on Java from https://github.com/Mojang/AccountsClient/

import requests
import json

AGENT = "minecraft"
PROFILE_URL = "https://api.mojang.com/profiles/page/{page}"

class ProfileCriteria(dict):
    def __init__(self, name, agent):
        self['name'] = name
        self['agent'] = agent

def get_uuid(name):
    crit = [ProfileCriteria(name, AGENT)]
    url = PROFILE_URL.format(page=1)
    data = json.dumps(crit)
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    r = requests.post(url, data=data, headers=headers)
    profiles = r.json()
    if 'profiles' in profiles:
        if profiles['size'] == 1:
            return profiles['profiles'][0]
    return None
