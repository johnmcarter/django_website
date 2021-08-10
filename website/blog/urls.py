# Created: 2021/08/07 21:15:16
# Last modified: 2021/08/09 22:16:34

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photos', views.photos, name='photos'),
    path('food_travel', views.food_travel, name='food_travel'),
    path('food_travel_blog/<int:post_id>/', views.food_travel_blog, name='food_travel_blog'),
]