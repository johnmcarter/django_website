'''
Created: 2021/08/07 21:15:16
Last modified: 2023/05/21 13:14:52
'''

from django.urls import path
from . import views

urlpatterns = [
    path('jjp_blog', views.jjp_blog, name='jjp_blog'),
    path('blog_post/<int:post_id>/', views.blog_post, name='blog_post'),
]
