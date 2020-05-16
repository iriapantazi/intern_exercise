#! /usr/bin/env python

import json
import requests
import re

from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

# constants
DELIVERY_MARKUPS = {
    "bicycle": 1.10,
    "motorbike": 1.15,
    "parsel_car": 1.20,
    "small_van": 1.30,
    "large_van": 1.40,
    "no vehicle": 1.00,
}


@app.route('/')
def welcome():
    """
    Simply print a welcome message.
    """
    msg = f'Welcome. Please append "/quotes" to the URL to get quotes.'
    return msg


@app.route('/quotes', methods = ['GET', 'POST'])
def quotes():
    """
    This function applies the request based on
    the method, i.e. 'GET' or 'POST'.
    """
    if request.method == 'POST':
        return quotes_post_handler(request)
    elif request.method == 'GET':
        return quotes_get_handler(request)


def quotes_get_handler(request):
    """
    Render html index page.
    """
    return render_template('index.html')


def quotes_post_handler(request):
    """
    This function creates the body of the request,
    and returns a response in json format.
    """
    
    body = request.get_json()
    try:
        pickup = body.get('pickup_postcode')
        delivery = body.get('delivery_postcode')
        vehicle = body.get('vehicle')
    except Exception as e:
        return(f'No valid body in post request was found. Stopping with error {e}.')
    
    # regex validation of input
    pickup, delivery, vehicle = validate_body_characters(pickup, delivery, vehicle)

    # default veficle will be 'no vehicle'
    if vehicle not in DELIVERY_MARKUPS:
        vehicle = 'no vehicle'
    
    vehicle_cost = DELIVERY_MARKUPS.get(vehicle, 1)

    # cost calculation
    cost = calculate_delivery_cost(pickup, delivery, vehicle_cost)

    # response construction
    response = construct_response_body(pickup, delivery, cost, vehicle)

    return jsonify(response)


def validate_body_characters(pick, deli, vehi):
    """
    This function removes characters that are not in the
    range a-z, A-Z, 0-9, so that the base-36 integer can be
    derived.
    """
    pick = re.sub(r'[^a-zA-Z0-9]', '', pick)
    deli = re.sub(r'[^a-zA-Z0-9]', '', deli)
    vehi = re.sub(r'[^a-zA-Z0-9]', '', vehi)
    return pick, deli, vehi


def calculate_delivery_cost(pickup, delivery, vehicle_cost=1):
    """
    This function calculates the delivery cost between pickup
    and delivery arguments. Both arguments should be strings.
    If result cannot be calculated because of a validation error,
    cost returned is always -1.
    """
    cost = 0
    try:
        cost = round((abs(int(delivery, base=36) - int(pickup, base=36)) * vehicle_cost) / 1E8 )
    except ValueError:
        cost = -1
    except Exception as e:
        cost = 'Error'
    return cost


def construct_response_body(pickup, delivery, price, vehicle='bicycle'):
    """
    This function constructs the body that will be posted.
    """
    data = {
        'pickup_postcode': pickup,
        'delivery_postcode': delivery,
        'price': price,
        'vehicle': vehicle,
    }
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
