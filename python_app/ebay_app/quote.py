#! /usr/bin/env python

import re

# constants
DELIVERY_MARKUPS = {
    "bicycle": 1.10,
    "motorbike": 1.15,
    "parsel_car": 1.20,
    "small_van": 1.30,
    "large_van": 1.40,
    "no vehicle": 1.00,
}

def class Quote:

    def __init__(self, body):
        self.body = body
        try:
            self.pickup = body.get('pickup_postcode')
            self.delivery = body.get('delivery_postcode')
            self.vehicle = body.get('vehicle')
            if self.vehicle not in DELIVERY_MARKUPS:
                self.vehicle = 'no vehicle'
            self.vehicle_cost = DELIVERY_MARKUPS.get(self.vehicle, 1)
        except Exception as e:
            print(f'No valid body in post request was found. Stopping with error {e}.')
            sys.exit(-1)


    def validate_body_characters(self):
        self.pickup = re.sub(r'[^a-zA-Z0-9]', '', pickup)
        self.delivery = re.sub(r'[^a-zA-Z0-9]', '', delivery)


    def calculate_delivery_cost(self):
        """
        This function calculates the delivery cost between pickup
        and delivery arguments. Both arguments should be strings.
        If result cannot be calculated because of a validation error,
        cost returned is always -1.
        """
        cost = 0
        try:
            cost = round((abs(int(self.delivery, base=36) - int(self.pickup, base=36)) * self.vehicle_cost) / 1E8 )
        except ValueError:
            cost = -1
        except Exception as e:
            cost = 'Error'
        return(cost)



    def construct_response_body(self, price):
        """
        This function constructs the body that will be posted.
        """
        data = {
            'pickup_postcode': self.pickup,
            'delivery_postcode': self.delivery,
            'price': price,
            'vehicle': self.vehicle,
        }
        return data
