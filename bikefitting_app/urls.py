"""
    contains all paths to different sites
"""

from django.contrib import admin
from django.urls import path

from bikefitting_app.views import index, upload

urlpatterns = [
    path('', index, name='index'),              # main-page
    path('admin/', admin.site.urls),            # admin-page
    path('upload/', upload, name='upload'),     # upload-page
]



