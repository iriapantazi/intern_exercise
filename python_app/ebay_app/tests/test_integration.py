#! /usr/bin/env python

import requests, pytest
import json

from app import DELIVERY_MARKUPS, calculate_delivery_cost



URL = 'http://127.0.0.1:5001/quotes'

p_data = {
        'pickup_postcode': 'aaaah',
        'delivery_postcode': 'aaaaaaa',
        'vehicle': 'bicycle'
        }

resp = requests.post(URL, json = p_data)

if resp.ok and resp.status_code == 200:
    print(f'The server is up.')
else:
    print(f'There was an error with error-code: {resp.status_code} and reason: {resp.reason}.')




@pytest.mark.parametrize('pick, deli, vehi, returned', 
                        [('SW1A1AA', 'EC2A3LT', 1.1, 349),
                         ('SW1A1AA', 'EC2A3LT', 1.0, 317),
                         ('222222222', '22233444444', 1, 75155175),
                         ('222222222', '22233---444444', 1, -1),
                         (222222222, 22233444444, 'yy', 'Error'),
                        ]
                         )
def test_calculate_delivery_cost(pick, deli, vehi, returned):
    expected = calculate_delivery_cost(pick, deli, vehi)
    assert expected == returned





