"""
    APPS
    Module for starting the different Apps
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""
from django.apps import AppConfig


class BikeFittingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bikefitting_app'