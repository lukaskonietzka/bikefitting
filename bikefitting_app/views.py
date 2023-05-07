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
    :param request:
    :return:            The index.html file to render
    """
    fittings = FittingForm()
    return render(request, 'index.html')


def upload(request):
    """
    Generating the "Upload" page
    :param request:
    :return:            The upload.html-file to render
    """
    form = FittingForm()  # leeres Formular
    return render(request, 'upload.html', dict(upload_form=form))
