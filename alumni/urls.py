from django.urls import path

from alumni import views

urlpatterns = [
    path('', views.alumni, name='alumni'),
]
