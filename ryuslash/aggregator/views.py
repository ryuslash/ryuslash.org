from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.shortcuts import render

from aggregator.models import Post


def _get_category(cat):
    if cat == 'activity':
        return 1
    else:
        return 0


def posts(request, cat, page=1):
    category = _get_category(cat)
    queryset = Post.objects.filter(feed__category=category)
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
