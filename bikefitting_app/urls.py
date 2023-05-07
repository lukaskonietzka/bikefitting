"""
    URLS
    Contains all paths to different sites from the app bikfitting_app
    Author:     Niehage, Sebastian
                Konietzka, Lukas
"""

from django.contrib import admin
from django.urls import path

from bikefitting_app.views import index, upload

urlpatterns = [
    path('', index, name='index'),              # main-page
    path('admin/', admin.site.urls),            # admin-page
    path('upload/', upload, name='upload'),     # upload-page
]



