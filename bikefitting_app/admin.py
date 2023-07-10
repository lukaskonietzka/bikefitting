"""
    ADMIN

    Admin-page to manage the database

    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django.contrib import admin
from .models import Fitting

admin.site.register(Fitting)
