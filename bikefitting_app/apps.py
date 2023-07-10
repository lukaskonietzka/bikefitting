"""
    BIKE-Fitting-APP

    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""
from django.apps import AppConfig


class BikeFittingConfig(AppConfig):
    """
        Class for app configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bikefitting_app'
