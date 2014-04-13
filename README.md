Install

```
pip install git+git://github.com/Thezomg/mcapi.git
```

Example

```python
from mcapi.profile import get_uuid

profiles = get_uuid('Deaygo')
if profiles is not None and len(profiles) > 0:
    print profiles[0]['id']
```

```python
from mcapi.profile import get_profile

profile = get_profile('2413639c21d64ba7a43ec90933f543e3')

if profile is not None:
    print profile['name']
```
