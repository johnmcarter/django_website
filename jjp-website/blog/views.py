'''
Copyright 2021 by John Carter
Created: 2021/08/07 21:12:00
Last modified: 2021/09/10 20:27:24
'''
from django.shortcuts import render
import boto3

from .models import BlogPost

PHOTO_URL = 'https://johnjohnphotos-media.s3.amazonaws.com'


def food_travel(request):
    '''
    Display listing of most current blog posts
    '''
    latest_post_list = BlogPost.objects.order_by('-pub_date')[:5]
    context = {
        'photo_url': PHOTO_URL,
        'latest_post_list': latest_post_list,
    }
    return render(request, 'food_travel_blogs.html', context)


def food_travel_blog(request, post_id):
    '''
    Display one blog post
    '''
    post = BlogPost.objects.get(id=post_id)
    context = {
        'photo_url': PHOTO_URL,
        'post': post
    }
    return render(request, 'blog_post.html', context)