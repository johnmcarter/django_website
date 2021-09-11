# Created: 2021/08/07 21:15:16
# Last modified: 2021/09/10 22:41:32

from django.urls import path
from . import views

urlpatterns = [
    path('jjp_blog', views.jjp_blog, name='jjp_blog'),
    path('blog_post/<int:post_id>/', views.blog_post, name='blog_post'),
]