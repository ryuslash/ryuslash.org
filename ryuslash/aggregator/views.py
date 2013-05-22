from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.shortcuts import render

from aggregator.models import CATEGORIES, Feed, Post


def posts(request, cat=None, page=1):
    category = cat or 'all'
    posts = Post.objects.all()
    feeds = Feed.objects.all()

    if category != 'all':
        posts = posts.filter(feed__category=CATEGORIES.index(category))
        feeds = feeds.filter(category=CATEGORIES.index(category))

    paginator = Paginator(posts, 20)

    if page is None:
        page = 1

    try:
        object_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        raise Http404

    ctx = {'list': object_list,
           'category': category,
           'feeds': feeds}

    return render(request, 'aggregator/posts.html', ctx)
