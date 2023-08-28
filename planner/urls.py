from . import views
from django.urls import path


urlpatterns = [
    path('', views.show_api, name='home')
]