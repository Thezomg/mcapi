Install

```
pip install git+git://github.com/Thezomg/mcapi.git
```

Example

```python
from mcapi.profile import get_uuid

profile = get_uuid('Deaygo')
if profile != None:
    print profile['id']
```
