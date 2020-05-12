#! /usr/bin/env python

import requests

URL = 'http://127.0.0.1:5001'

resp = requests.get(URL)
sts = resp.status_code

if resp.ok and sts == 200:
    print(f'The server is up.')
else:
    print(f'There was an error with error code {sts}.')