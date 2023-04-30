""" Contains all Pages """

from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from src import models


class FittingForm(forms.ModelForm):
    """ Klasse zur Formularerstellung.
        Aus Vorlage des Dozenten
    """
    class Meta:
        model = models.Fitting
        exclude = []


def upload(request):
    """
    Vorlage des Dozenten
    :param request:
    :return:
    """
    # werden Formulardaten geschickt?
    if request.method == "POST":
        form = FittingForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            new_Fitting = form.save()
            return HttpResponseRedirect('/gallery/')  # Umleitung
    else:
        form = FittingForm()  # leeres Formular
    return render(request, 'upload.html', dict(upload_form=form))
