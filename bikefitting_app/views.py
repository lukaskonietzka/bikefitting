"""
    FRONTEND
    Contains all page for the website, every method
    returns a html-file to render
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from bikefitting_app import models
from bikefitting_app.models import Roadbike, Mountainbike, Trekkingbike
from bikefitting_app.models import Fitting


class FittingForms(ModelForm):
    class Meta:
        model = Fitting
        fields = '__all__'
        #fields = ('Name', 'Height', 'Step Length',)


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
    # TODO
    # Wie kann man daten berechnen und in das Datenmodel schreiben?

    form = FittingForms()
    data = request.session.get('data')

    if request.method == 'POST':
        form = FittingForms(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    if data == 1:
        rb = Roadbike()
    elif data == 2:
        mb = Mountainbike()
    elif data == 3:
        tb = Trekkingbike()

    return render(request, 'inputData.html', context)

def results(request):
    """
    Generating the "result" page
    and read the necessary data from the Database
    :param request:     Data from the html file
    :return:            The results.html file ti render
    """
    # TODO
    # Warum werden die Daten nicht ausgegeben
    # greift auf das Datenmodell zu und gibt den Inhalt an die html weiter
    # Verwende immere den Namen, der In den Parametern beim Model angegeben werden.

    fittings = Fitting.objects.all()
    return render(request, 'results.html', dict(fittings=fittings))

def error(request):
    """
    Is always called, when an error appears.
    :param request:
    :return:
    """
    return render(request, 'error.html')
