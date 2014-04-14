## Based on Java from https://github.com/Mojang/AccountsClient/

import requests
import json

AGENT = "minecraft"
PROFILE_URL = "https://api.mojang.com/profiles/minecraft"
UUID_PROFILE_URL = 'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}'

class ProfileCriteria(dict):
    def __init__(self, name, agent):
        self['name'] = name
        self['agent'] = agent

def get_profile(uuid, timeout=10):
    url = UUID_PROFILE_URL.format(uuid=uuid)
    try:
        r = requests.get(url, timeout=timeout)
        profile = r.json()
    except:
        profile = None

    return profile

def get_uuid(*name, **kwargs):
    timeout = 10
    if "timeout" in kwargs:
        timeout = kwargs["timeout"]
    if len(name) == 0:
        return None
    p = []

    page = 1
    while True:
        if len(name) == 0:
            break
        crit = name[:100]
        name = name [100:]
        data = json.dumps(crit)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        r = requests.post(PROFILE_URL, data=data, headers=headers, timeout=timeout)
        profiles = r.json()
        p.extend(profiles)

        page += 1
                
    return p
