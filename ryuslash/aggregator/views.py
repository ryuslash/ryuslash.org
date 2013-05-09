from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.shortcuts import render

from aggregator.models import Post


def posts(request, cat, page=1):
    category = cat or 'post'
    queryset = Post.objects.filter(category=category)
    paginator = Paginator(queryset, 20)

    if page is None:
        page = 1

    try:
        object_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        raise Http404

    return render(request, 'aggregator/posts.html',
                  {'list': object_list,
                   'category': category})
