# Created: 2021/08/07 21:15:16
# Last modified: 2021/09/09 22:02:18

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photos', views.photos, name='photos'),
    path('display_photos/<str:id>', views.display_photos, name='display_photos'),
    path('cars', views.cars, name='cars'),
]