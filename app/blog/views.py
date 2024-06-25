'''
Copyright 2024 by John Carter
'''
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
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
    post = get_object_or_404(BlogPost, id=post_id)

    # Get next and previous posts based on reverse pub_date ordering
    next_post = BlogPost.objects.filter(
        Q(pub_date__lt=post.pub_date) | 
        Q(pub_date=post.pub_date, id__lt=post_id)
    ).order_by('-pub_date', '-id').first()

    previous_post = BlogPost.objects.filter(
        Q(pub_date__gt=post.pub_date) | 
        Q(pub_date=post.pub_date, id__gt=post_id)
    ).order_by('pub_date', 'id').first()

    context = {
        'photo_url': PHOTO_URL,
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post
    }
    return render(request, 'blog_post.html', context)
