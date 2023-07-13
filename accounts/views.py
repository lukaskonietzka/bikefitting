"""
    VIEW-METHODS

    Contains all page for the user login, every method
    returns a html-file to render

    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index_view(request):
    """
    Returns the index account-page
    This page is a child of the base.html.
    :param request:     Data from the html file
    :return:            accountsIndex.html to render
    """
    return render(request, 'accountsIndex.html')


@login_required()
def dashboard_view(request):
    """
    Returns the dashboard-page.
    :param request:     Data from the html file
    :return:            dashboard.html to render
    """
    return render(request, 'dashboard.html')


def register_view(request):
    """
    Return the registration-page
    :param request: Data from the html file
    :return:        register.html
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
