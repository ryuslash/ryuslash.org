from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.shortcuts import render_to_response

from .models import Post, Feed

def posts(request, page=1):
    queryset = Post.objects.all()
    feeds = Feed.objects.all()
    paginator = Paginator(queryset, 20)

    if page == None:
        page = 1

    try:
        object_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        raise Http404

    return render_to_response('aggregator/posts.html',
                              { 'list': object_list,
                                'feeds': feeds })
