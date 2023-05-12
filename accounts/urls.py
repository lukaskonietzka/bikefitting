from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login', LoginView.as_view()),     # upload-page
    path('logout', LogoutView.as_view()),            # admin-page
]