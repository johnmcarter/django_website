"""
Copyright 2021 by John Carter
Created: 2021/08/07 21:12:00
Last modified: 2023/06/25 18:25:13
"""
from django.db import models


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField("date published")
    location = models.CharField(max_length=200)
    website = models.URLField()
    image = models.ImageField(upload_to="blog_images/")
