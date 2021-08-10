# Created: 2021/08/07 21:12:00
# Last modified: 2021/08/09 22:38:01

from django.db import models


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200)
    content = models.TextField()
    photo_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')