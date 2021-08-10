# Created: 2021/08/07 21:12:00
# Last modified: 2021/08/09 19:20:15

from django.contrib import admin

from .models import BlogPost

admin.site.register(BlogPost)