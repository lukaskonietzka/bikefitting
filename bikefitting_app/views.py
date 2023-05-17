"""
    FRONTEND
    Contains all page for the website, every method
    returns a html-file to render
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from bikefitting_app import models
from bikefitting_app.models import Roadbike, Mountainbike, Trekkingbike
from .models import Fitting


def index(request):
    """
    Generating the "Start" page
    and give the user an instruction how the website works.
    :param request:     Data from the html file
    :return:            The index.html file to render
    """
    return render(request, 'index.html')

def selectBike(request):
    """
    Generating the "select Bike" page
    and creat the object that is needed.
    :param request:     Data from the html file
    :return:            The selectBike.html file to render
    """
    if request.method == 'POST':
        button_value = request.POST.get('name of this button')
        if button_value == 'roadBike':
            request.session['data'] = 1
        elif button_value == 'mountainBike':
            request.session['data'] = 2
        elif button_value == 'trekkingBike':
            request.session['data'] = 3
        else:
            return render(request, 'error.html')
    return render(request, 'selectBike.html')

def measureStepLenght(request):
    """
    Generating the "Measure" page
    and give an instruction how to measure step length
    :param request:     Data from the html file
    :return:            The measureStepLenght.html-file to render
    """
    return render(request, 'measureStepLenght.html')


def inputData(request):
    """
    Generating the "Input" page
    And calls the creatFitting()-Methode on an object.
    This method is writing the data from the input into the database.
    :param request:     Data from the html file
    :return:            The inputData.html file to render
    """
    data = request.session.get('data')

    if request.method == 'POST':
        name = request.POST.get('name of this field')
        height = request.POST.get('name of this field')
        step_length = request.POST.get('name of this field')

    if data == 1:
        rb = Roadbike()
        rb.create_roadbike_fitting(name, height, step_length)
    elif data == 2:
        mb = Mountainbike()
        mb.create_mountainbike_fitting(name, height, step_length)
    elif data == 3:
        tb = Trekkingbike()
        tb.create_trekkingbike_fitting(name, height, step_length)
    else:
        return render(request, 'error.html')
    return render(request, 'inputData.html')

def results(request):
    """
    Generating the "result" page
    and read the necessary data from the Database
    :param request:     Data from the html file
    :return:            The results.html file ti render
    """
    data = Fitting.objects.all()

    # TODO greift auf das Datenmodell zu und gibt den Inhalt an die html weiter
    return render(request, 'results.html', {'data': data})

def error(request):
    """
    Is always called, when an error appears.
    :param request:
    :return:
    """
    return render(request, 'error.html')
