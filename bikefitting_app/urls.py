"""
    URL-BIKE_FITTING-APP

    URL configuration for bikefitting_app.
    Contains all paths to different sites from the app bikfitting_app

    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django.urls import path
from bikefitting_app.views import index, measure_step_length, select_bike, input_data, results, error, search_results

urlpatterns = [
    path('', index, name='index'),
    path('measureStepLenght', measure_step_length, name='measureStepLenght'),
    path('selectBike', select_bike, name='selectBike'),
    path('inputData', input_data, name='inputData'),
    path('results', results, name='results'),
    path('error', error, name='error'),
    path('search/', search_results, name='search_results'),
]




