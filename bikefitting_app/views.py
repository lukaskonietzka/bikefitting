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
    def __int__(self):
        self.fields['Name'].required = False
    class Meta:
        model = Fitting
        # fields = '__all__'
        fields = ('Name', 'Height', 'StepLength',)




def index(request):
    """
    Generating the "Start" page
    and give the user an instruction how the website works.
    :param request:     Data from the html file
    :return:            The index.html file to render
    """
    #TODO Hier current-bike auf null setzen
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
        if len(bikes) != 1:
            current_bike = None
            return render(request, 'error.html', show_message("Bitte wählen Sie zuerst ein Fahrrad aus"))
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
    form_class = FittingForms
    form = FittingForms(request.POST)
    if request.POST:
        name = request.POST['Name']
        height = int(request.POST['Height'])
        step_length = int(request.POST['StepLength'])
        input_from_user = (name, height, step_length)
        request.session['data'] = input_from_user
        if form.is_valid():
            form.save()
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

    fittings = Fitting.objects.last()
    name = request.session.get('data')[0]
    height = request.session.get('data')[1]
    step_length = request.session.get('data')[2]

    if current_bike == None:
        return render(request, 'error.html')

    if current_bike == 'rb':
        rb = Roadbike()
        name, height, step_length, frame_height, saddle_height = rb.create_roadbike_fitting(name, height, step_length)
    elif current_bike == 'mb':
        mb = Mountainbike()
        name, height, step_length, frame_height, saddle_height = mb.create_mountainbike_fitting(name, height, step_length)
    elif current_bike == 'tb':
        tb = Trekkingbike()
        name, height, step_length, frame_height, saddle_height = tb.create_trekkingbike_fitting(name, height, step_length)
    else:
        return render(request, 'error.html', show_message("An einer Stelle fehlen noch Daten, bitte überprüfen Sie Ihre eingabe."))
    return render(request, 'results.html', dict(fittings=fittings, frame_height=frame_height, saddle_height=saddle_height))


def error(request):
    """
    Is always called, when an error appears.
    :param request:
    :return:
    """

    return render(request, 'error.html')


def error404(request):
    #TODO: Create an 404-Page and turn of the debug-mode
    pass


def show_message(message):
    """
    Returns a dict with the given parameter
    to show an error-Message
    :param message:
    :return:
    """

    return dict(message=message)
