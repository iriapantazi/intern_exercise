#! /usr/bin/env python

import json
import requests
from flask import Flask, request, render_template, jsonify

from quote import Quote

app = Flask(__name__)


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

    a_quote = Quote(body)
    a_quote.validate_body_characters()
    cost = a_quote.calculate_delivery_cost()
    response = a_quote.construct_response_body(cost)

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
