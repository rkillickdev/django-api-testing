from . import views
from django.urls import path

# app_name = 'planner'

urlpatterns = [
    path('', views.show_api, name='home'),
    path('add/<str:attraction>/', views.add_place, name='API-add')
]