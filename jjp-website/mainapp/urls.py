'''
Created: 2021/08/07 21:15:16
Last modified: 2023/06/16 21:20:43
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('travel', views.travel, name='travel'),
    path('display_photos/<str:id>', views.display_photos, name='display_photos'),
    path('cars', views.cars, name='cars'),
    path('research', views.research, name='research'),
]
