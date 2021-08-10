# Created: 2021/08/07 21:12:00
# Last modified: 2021/08/09 22:25:40

from django.shortcuts import render

from .models import BlogPost

PHOTO_URL = 'https://johnjohnphotos-media.s3.amazonaws.com'


def index(request):
    context = {
        'photo_url': PHOTO_URL
    }
    return render(request, 'index.html', context)


def photos(request):
    context = {
        'photo_url': PHOTO_URL
    }
    return render(request, 'photos.html', context)


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