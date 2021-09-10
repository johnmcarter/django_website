'''
Copyright 2021 by John Carter
Created: 2021/08/07 21:12:00
Last modified: 2021/09/09 22:08:07
'''
from django.db import models


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200)
    content = models.TextField()
    photo_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')