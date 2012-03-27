from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Post, Feed, Category

def posts(request, cat, page=1):
    category = cat or 'posts'
    queryset = Post.objects.filter(feed__categories__name=category)
    feeds = Feed.objects.filter(categories__name=category)
    paginator = Paginator(queryset, 20)

    if page == None:
        page = 1

    try:
        object_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        raise Http404

    return render(request, 'aggregator/posts.html',
                  { 'list': object_list,
                    'feeds': feeds,
                    'category': category,
                    'categories': Category.objects.order_by('name') })
