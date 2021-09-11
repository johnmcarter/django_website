'''
Copyright 2021 by John Carter
Created: 2021/09/09 21:59:00
Last modified: 2021/09/10 22:24:29
'''
from django.shortcuts import render
import boto3

PHOTO_URL = 'https://johnjohnphotos-media.s3.amazonaws.com'


def index(request):
    context = {
        'photo_url': PHOTO_URL
    }
    return render(request, 'index.html', context)


def travel(request):
    context = {
        'photo_url': PHOTO_URL
    }
    return render(request, 'travel.html', context)


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