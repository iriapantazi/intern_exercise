#! /usr/bin/env python

import json
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

# constants
DELIVERY_MARKUPS = {
    "bicycle": 1.10,
    "motorbike": 1.15,
    "parsel_car": 1.20,
    "small_van": 1.30,
    "large_van": 1.40,
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
    #if not ('pickup_postcode' in body.keys() or 'delivery_postcode' in body.keys() or 'vehicle' in body.keys()):
    #    msg = (f'No valid input was provided.')
    pickup = body.get('pickup_postcode')
    delivery = body.get('delivery_postcode')
    vehicle = body.get('vehicle')
    if vehicle not in DELIVERY_MARKUPS:
        msg = (f'Vehicle type {vehicle} is not valid, hence the cost of delivery through'
        ' this vehicle is not taken under consideration in the cost calculation.')
        vehicle = 'bicycle'
    vehicle_cost = DELIVERY_MARKUPS.get(vehicle, 1)
    cost = calculate_delivery_cost(pickup, delivery, vehicle_cost)
    response = construct_response_body(pickup, delivery, cost, vehicle)
    return jsonify(response)


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
