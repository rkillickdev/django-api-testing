from django.shortcuts import render
from django.http.response import HttpResponse

import os
if os.path.isfile('env.py'):
    import env

# Install the Python library from https://pypi.org/project/amadeus
from amadeus import Client, ResponseError, Location

# Create your views here.


def show_api(request):

    amadeus = Client(
        client_id=os.environ.get('AMADEUS_API_KEY'),
        client_secret=os.environ.get('AMADEUS_API_SECRET')
    )

    try:
        '''
        What are the popular places in Barcelona (based on a geo location and a radius)
        '''
        response = amadeus.reference_data.locations.points_of_interest.get(latitude=41.397158, longitude=2.160873)
        attractions = response.data

        context = {
            'attractions': attractions
        }

    except ResponseError as error:
        raise error

    return render(request, 'index.html', context)
