'''
Created: 2021/08/07 21:12:00
Last modified: 2023/05/21 20:34:20
'''

from django.contrib import admin

from .models import BlogPost

admin.site.register(BlogPost)
