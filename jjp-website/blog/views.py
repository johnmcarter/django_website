'''
Copyright 2023 by John Carter
Created: 2021/08/07 21:12:00
Last modified: 2023/05/26 21:22:32
'''
from django.shortcuts import render

from .models import BlogPost

PHOTO_URL = 'https://johnjohnphotos-media.s3.amazonaws.com'


def jjp_blog(request):
    '''Display listing of most current blog posts'''
    posts = BlogPost.objects.order_by('-pub_date')[:10]
    context = {
        'photo_url': PHOTO_URL,
        'posts': posts,
    }
    return render(request, 'jjp_blogs.html', context)


def blog_post(request, post_id):
    '''Display one blog post'''
    post = BlogPost.objects.get(id=post_id)
    context = {
        'photo_url': PHOTO_URL,
        'post': post
    }
    return render(request, 'blog_post.html', context)
