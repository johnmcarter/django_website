"""
Copyright 2024 by John Carter
"""
from django.shortcuts import render
import boto3

from .models import ResearchPaper, Car
from blog.models import BlogPost

PHOTO_URL = "https://johnjohnphotos-media.s3.amazonaws.com"


def index(request):
    """Show homepage"""
    posts = BlogPost.objects.order_by('-pub_date')[:3]  
    papers = ResearchPaper.objects.order_by('-date')[:4]  

    context = {
        'photo_url': PHOTO_URL,
        'posts': posts,
        'papers': papers,
    }
    return render(request, 'index.html', context)


def travel(request):
    """Show travel page"""
    context = {"photo_url": PHOTO_URL}
    return render(request, "travel.html", context)


def display_photos(request, id):
    header = id.title().replace("_", " ")

    try:
        s3_resource = boto3.resource("s3")
        photo_bucket = s3_resource.Bucket("johnjohnphotos-media")

        image_list = [
            file.key
            for file in photo_bucket.objects.all()
            if id in file.key and len(file.key.split(".")) == 2
        ]

        context = {"photo_url": PHOTO_URL, "image_list": image_list, "header": header}
        return render(request, "display_photos.html", context)
    
    except Exception as e:
        print(f"Error accessing S3 bucket: {e}")
        context = {"header": header, "error": "Unable to retrieve photos. Please try again later 😕"}
        return render(request, "display_photos.html", context)


def cars(request):
    """Show car page"""
    context = {"photo_url": PHOTO_URL, "cars": Car.objects.all()}
    return render(request, "cars.html", context)


def research(request):
    """Show research page"""
    context = {
        "photo_url": PHOTO_URL,
        "papers": ResearchPaper.objects.order_by("-date"),
    }
    return render(request, "research.html", context)
