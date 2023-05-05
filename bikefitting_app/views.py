"""
    FRONTEND
    Contains all page for the website
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from bikefitting_app import models


class FittingForm(forms.ModelForm):
    """ Klasse zur Formularerstellung.
        Aus Vorlage des Dozenten
    """
    class Meta:
        model = models.Fitting
        exclude = []


def index(request):
    fittings = FittingForm()
    return render(request, 'index.html')


def upload(request):
    form = FittingForm()  # leeres Formular
    return render(request, 'upload.html', dict(upload_form=form))
