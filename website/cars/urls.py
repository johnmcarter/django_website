# Created: 2021/07/24 21:27:50
# Last modified: 2021/07/24 21:28:05

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]