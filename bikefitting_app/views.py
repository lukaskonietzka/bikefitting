"""
    FRONTEND
    Contains all page for the website, every method
    returns a html-file to render
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from bikefitting_app.models import Roadbike, Mountainbike, Trekkingbike
from bikefitting_app.models import Fitting


class FittingForms(ModelForm):
    name = forms.TextInput()
    height = forms.TextInput()
    step_length = forms.TextInput()
    frame_height = forms.TextInput()
    saddle_height = forms.TextInput()

    class Meta:
        model = Fitting
        # fields = '__all__'
        fields = ('Name', 'Height', 'Step Length',)



def index(request):
    """
    Generating the "Start" page
    and give the user an instruction how the website works.
    :param request:     Data from the html file
    :return:            The index.html file to render
    """
    return render(request, 'index.html')


@login_required()
def selectBike(request):
    """
    Generating the "select Bike" page
    and creat the object that is needed.
    If more types are selected, we switch to the error-page
    :param request:     Data from the html file
    :return:            The selectBike.html file to render
    """
    global current_bike
    if request.POST:
        bikes = request.POST.getlist('bike')
        if len(bikes) > 1:
            return render(request, 'error.html')
        current_bike = bikes[0]
    return render(request, 'selectBike.html')


@login_required()
def measureStepLenght(request):
    """
    Generating the "Measure" page
    and give an instruction how to measure step length
    :param request:     Data from the html file
    :return:            The measureStepLenght.html-file to render
    """
    return render(request, 'measureStepLenght.html')


@login_required()
def inputData(request):
    """
    Generating the "Input" page
    And calls the creatFitting()-Methode on an object.
    This method is writing the data from the input into the database.
    If you type in another value, we throw an Exception.
    :param request:     Data from the html file
    :return:            The inputData.html file to render
    """
    form = FittingForms(request.POST)
    if request.POST:
        name = request.POST['Name']
        height = int(request.POST['Height'])
        step_length = int(request.POST['Step Length'])
        if current_bike == 'rb':
            rb = Roadbike()
            print('RB', rb.create_roadbike_fitting(name, height, step_length))
        elif current_bike == 'mb':
            mb = Mountainbike()
            print('MB', mb.create_mountainbike_fitting(name, height, step_length))
        elif current_bike == 'tb':
            tb = Trekkingbike()
            print('TB', tb.create_trekkingbike_fitting(name, height, step_length))
        else:
            return render(request, 'error.html')
    return render(request, 'inputData.html', {'form': form})


@login_required()
def results(request):
    """
    Generating the "result" page
    and read the necessary data from the Database
    :param request:     Data from the html file
    :return:            The results.html file ti render
    """
    # greift auf das Datenmodell zu und gibt den Inhalt an die html weiter
    # Verwende immer den Namen, der In den Parametern beim Model angegeben werden.

    fittings = Fitting.objects.all()
    return render(request, 'results.html', dict(fittings=fittings))


def error(request):
    """
    Is always called, when an error appears.
    :param request:
    :return:
    """
    return render(request, 'error.html')
