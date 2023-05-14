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

CURRENT_FITTING = None


class FittingForm(forms.ModelForm):
    """ Klasse zur Formularerstellung.
        Aus Vorlage des Dozenten
    """

    class Meta:
        model = models.Fitting
        exclude = []


def index(request):
    """
    Generating the "Start" page
    and give the user an instruction how the website works.
    :param request:     Data from the html file
    :return:            The index.html file to render
    """
    fittings = FittingForm()
    return render(request, 'index.html')


def selectBike(request):
    """
    Generating the "select Bike" page
    and creat the object that is needed.
    :param request:     Data from the html file
    :return:            The selectBike.html file to render
    """
    if request.method == 'POST':
        button_value = request.POST.get('button')
        if button_value == 'roadBike':
            rb = Roadbike()
            global rb
        elif button_value == 'mountainBike':
            mb = Mountainbike()
            global  mb
        elif button_value == 'trekkingBike':
            tb = Trekkingbike()
            global tb
        else:
            #TODO html-Seite für Fehlermeldung error.html
            pass
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
    :param request:     Data from the html file
    :return:            The inputData.html file to render
    """
    # TODO holt die Daten aus dem input und
    #  ruft die methode creatFitting auf und schreibt damit in die Datenbank
    return render(request, 'inputData.html')


def results(request):
    """
    Generating the "result" page
    and read the necessary data from the Database
    :param request:     Data from the html file
    :return:            The results.html file ti render
    """
    # TODO greift auf das Datenmodell zu und gibt den Inhalt an die html weiter
    return render(request, 'results.html')
