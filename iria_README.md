# Web app for cost quotes in python

## Introduction

This is an exercise that simulates a hypothetical quoting engine that 
according to the input provided, it returns an output. The exercise creates 
a RESTful API endpoint that takes a few details and works out the price for 
a delivery.

The user posts a json file with information on the pickup and delivery points, 
along with the transportation method. The post request for example can be:
```
{
  "pickup_postcode":   "SW1A1AA",
  "delivery_postcode": "EC2A3LT",
  "vehicle": "bicycle"
}
```
and the response from the server will be:
```
{
  "pickup_postcode":   "SW1A1AA",
  "delivery_postcode": "EC2A3LT"
  "vehicle": "bicycle"
  "price": 348
}
```
The price is calculated by the absolute value of the difference of the base-36 
integers derived by the post code strings, when a transportation cost is added, 
and divided by `1E8`. 
The transportation cost is calulated as follows:

* bicycle: 10%
* motorbike: 15%
* parcel_car: 20%
* small_van: 30%
* large_van: 40%

## Getting Started

You can run the application in a container with the use of docker and docker-compose. 
Simply run the following commands: 

  `sudo docker-compose build ` for building the docker image, and 

  `sudo docker-compose up -d ` for running the application in the background.


In case you want to run the application without docker, it is suggested that you 
create a virtual environment, and use python 3.8. Older versions of python may be 
used, but this has not been tested so far. Install the required packages by executing
 `pip install -r requirements.txt`. After all the packages have been 
 successfully installed, execute `python ebay_app/app.py`

### Prerequisites
You will need
 - python3.8 (older versions have not been tested yet)
 - virtualenv
 - docker
 -docker-compose

## Runnig the tests
You can run the tests by executing from the python-app directory  
 `python -m unittest ebay_app/test_app.py`



## Code organisation tree
The tree of the code organisation is the following:
```
.
├── iria_README.md
├── python_app
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── ebay_app
│   │   ├── app.py
│   │   ├── __init__.py
│   │   ├── templates
│   │   │   └── index.html
│   │   └── tests
│   │       └── test_app.py
│   └── requirements.txt
└── README.md
```
