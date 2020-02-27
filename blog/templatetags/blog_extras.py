# -*- coding:utf-8 -*-
from django import template
from ..models import Category, Tag, Post

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    post_list = Post.objects.all().order_by('-created_time')[:num]
    return {'recent_post_list': post_list}


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    date_list = Post.objects.dates('created_time', 'month', order='DESC')
    return {'date_list': date_list}


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }
