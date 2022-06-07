from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import blog

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_blog_without_cache():
    return list(blog.objects.all())


def get_blog_with_cache():
    if 'blogs' in cache:
        blogs = cache.get('blogs')
    else:
        blogs = list(blog.objects.all())
        cache.set('blogs', blogs, timeout=CACHE_TTL)
    return blogs


@cache_page(CACHE_TTL)
def blog_view(request):
    blog = get_blog_with_cache()
    print(blog)
    return HttpResponse(
        blog
    )