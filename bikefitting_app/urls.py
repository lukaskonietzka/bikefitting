"""
    URLS
    Contains all paths to different sites from the app bikfitting_app
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django.contrib import admin
from django.urls import path

from bikefitting_app.views import index, measureStepLenght, selectBike, inputData, results, error

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index, name='index'),
    path('measureStepLenght', measureStepLenght, name='measureStepLenght'),
    path('selectBike', selectBike, name='selectBike'),
    path('inputData', inputData, name='inputData'),
    path('results', results, name='results'),
    path('error', error, name='error'),
]



