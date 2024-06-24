'''
Copyright 2024 by John Carter
'''
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import BlogPost

PHOTO_URL = 'https://johnjohnphotos-media.s3.amazonaws.com'


def jjp_blog(request):
    '''Display listing of most current blog posts'''
    post_list = BlogPost.objects.order_by('-pub_date')
    paginator = Paginator(post_list, 6)  

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'photo_url': PHOTO_URL,
        'posts': posts,
    }
    return render(request, 'jjp_blogs.html', context)


def blog_post(request, post_id):
    '''Display one blog post'''
    post = BlogPost.objects.get(id=post_id)
    context = {
        'photo_url': PHOTO_URL,
        'post': post
    }
    return render(request, 'blog_post.html', context)
