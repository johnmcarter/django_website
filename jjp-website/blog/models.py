'''
Copyright 2021 by John Carter
Created: 2021/08/07 21:12:00
Last modified: 2021/09/10 20:20:22
'''
from django.db import models


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='blog_images/')