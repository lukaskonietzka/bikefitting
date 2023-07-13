"""
    VIEW-METHODS

    Contains all page for the website,
    every method returns a html-file to render

    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django.forms import ModelForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bikefitting_app.models import Roadbike, Mountainbike, Trekkingbike
from bikefitting_app.models import Fitting


class FittingForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].required = True
        self.fields['Height'].required = True
        self.fields['StepLength'].required = True

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
    global current_bike
    current_bike = None
    return render(request, 'index.html')


@login_required()
def select_bike(request):
    """
    Generating the "select Bike" page
    and creat the object that is needed.
    If more types are selected, we switch to the error-page
    An login is required.
    :param request:     Data from the html file
    :return:            The selectBike.html file to render
    """
    global current_bike
    if request.POST:
        bikes = request.POST.getlist('bike')
        if len(bikes) != 1:
            current_bike = None
            return render(request, 'error.html',
                          show_message("Bitte wählen Sie zuerst ein Fahrrad aus und drücken sie dann auf Abschicken."))
        current_bike = bikes[0]
    return render(request, 'selectBike.html')


@login_required()
def measure_step_length(request):
    """
    Generating the "Measure" page
    and give an instruction how to measure step length
    An login is required.
    :param request:     Data from the html file
    :return:            The measureStepLenght.html-file to render
    """
    return render(request, 'measureStepLenght.html')


@login_required()
def input_data(request):
    """
    Generating the "Input" page
    And calls the creatFitting()-Methode on an object.
    This method is writing the data from the input into the database.
    A login is required.
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
        if name is None or step_length is None or step_length is None:
            return render(request, 'error.html',
                          show_message("An einer Stelle fehlen noch Daten, bitte überprüfen Sie Ihre Eingabe."))
        if form.is_valid():
            form.save()
    return render(request, 'inputData.html', {'form': form})


@login_required()
def results(request):
    """
    Generating the "result" page
    and read the necessary data from the Database
    An login is required.
    :param request:     Data from the html file
    :return:            The results.html file to render
    """
    if request.session.get('data') is None:
        return render(request, 'error.html',
                      show_message("Befor sie ein Ergebnis erhalten können, müssen sie ein Fitting konfigurieren."))

    fittings = Fitting.objects.last()
    name = request.session.get('data')[0]
    height = request.session.get('data')[1]
    step_length = request.session.get('data')[2]

    if current_bike is None:
        return render(request, 'error.html',
                      show_message("An einer Stelle fehlen noch Daten, bitte überprüfen Sie Ihre Eingabe."))

    if current_bike == 'rb':
        rb = Roadbike()
        frame_height, saddle_height, bike_type = rb.create_roadbike_fitting(name, height, step_length)
    elif current_bike == 'mb':
        mb = Mountainbike()
        frame_height, saddle_height, bike_type = mb.create_mountainbike_fitting(name, height, step_length)
    elif current_bike == 'tb':
        tb = Trekkingbike()
        frame_height, saddle_height, bike_type = tb.create_trekkingbike_fitting(name, height, step_length)
    else:
        return render(request, 'error.html')
    return render(request, 'results.html', dict(fittings=fittings,
                                                frame_height=frame_height,
                                                saddle_height=saddle_height,
                                                bike_typ=bike_type))


def error(request):
    """
    Is always called, when an error appears.
    :param request: Date from the htm file
    :return:        the error.html page to render
    """
    return render(request, 'error.html')


def handle_404(request, exception):
    """
    if a 404 error appears, we route to the error page
    :param request:     Date form the html page
    :param exception:   Exceptions from the html page
    :return:            The error404.html page to render
    """
    return render(request, 'error404.html')


def handle_500(request):
    """
    If a 500 error appears, we route to the error page.
    :param request:     Data from the html-file
    :return:            The error.html page to render
    """
    return render(request, 'error.html',
                  show_message("Diese Seite sollten sie nicht sehen :(."))


def search_results(request):
    """
    Returns all objects that we found in
    the database
    :param request:     Data from the html-file
    :return:            The search_result.html page tu render all results
    """
    query = request.GET.get('query')
    results = Fitting.objects.filter(Name__icontains=query)
    return render(request, 'search_results.html', {'results': results})


def show_message(custom_message):
    """
    Returns a dict with the given parameter
    to show a custom message on each error-Message
    :param custom_message:
    :return:
    """
    base_message = ""
    message = base_message + custom_message
    return dict(message=message)
