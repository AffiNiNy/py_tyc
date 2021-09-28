import json
import os
import requests

r = requests.get('http://www.baidu.com')
header = r.headers
print(header)
print()

h = json.dumps(dict(header))

jsonPath = os.getcwd() + r'\website_info\headers\bd_header.json'
with open(jsonPath, 'w') as f:
    f.write(h)