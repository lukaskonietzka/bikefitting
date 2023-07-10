"""
    FRONTEND
    Contains all page for the user login, every method
    returns a html-file to render
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, 'accountsIndex.html')


@login_required()
def dashboard_view(request):
    return render(request, 'dashboard.html')


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
