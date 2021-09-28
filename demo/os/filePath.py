import json
import os

# filePath = os.getcwd() + r'\demo\os\cookies.txt'
filePath = os.getcwd() + '\website_info\headers\\bd_header.json'
print(filePath)
print()

with open(filePath, 'r') as cookieFile:
    read_data = cookieFile.read()
    rData = json.loads(read_data)
    print(type(rData))
    print('-----------')
    print(rData['Cache-Control'])
    