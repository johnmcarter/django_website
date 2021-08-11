# Created: 2021/08/07 21:12:00
# Last modified: 2021/08/10 18:44:22

from django.shortcuts import render
import boto3

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


def display_photos(request, id):
    '''
    Display photos from a folder by filtering using the id passed in
    '''
    header = id.title().replace('_', ' ')
    photo_bucket = boto3.resource('s3').Bucket('johnjohnphotos-media')
    image_list = [file.key for file in photo_bucket.objects.all() if id in file.key]
    context = {
        'photo_url': PHOTO_URL,
        'image_list': image_list,
        'header': header
    }
    return render(request, 'display_photos.html', context)


def cars(request):
    context = {
        'photo_url': PHOTO_URL
    }
    return render(request, 'cars.html', context)


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