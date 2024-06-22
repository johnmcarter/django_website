"""
Copyright 2023 by John Carter
Created: 2021/09/09 21:59:00
Last modified: 2023/06/27 21:41:18
"""
from django.shortcuts import render
import boto3

from .models import ResearchPaper, Car

PHOTO_URL = "https://johnjohnphotos-media.s3.amazonaws.com"


def index(request):
    """Show homepage"""
    context = {"photo_url": PHOTO_URL}
    return render(request, "index.html", context)


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
