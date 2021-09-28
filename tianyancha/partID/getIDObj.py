import json
import os
import sys
sys.path.append(os.path.split(sys.path[0])[0])
from argparse import Namespace

def get_idObjs():
    with open('tianyancha/partID/ids.json', "r", encoding='utf8') as f1:
        return json.loads(f1.read(), object_hook=lambda d: Namespace(**d))