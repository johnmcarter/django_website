# Created: 2021/08/07 21:15:16
# Last modified: 2021/09/09 22:02:10

from django.urls import path
from . import views

urlpatterns = [
    path('food_travel', views.food_travel, name='food_travel'),
    path('food_travel_blog/<int:post_id>/', views.food_travel_blog, name='food_travel_blog'),
]