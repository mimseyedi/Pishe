from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post, BlogCategory, BlogTag


def blog_home_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    last_posts = posts[:3]
    categories = BlogCategory.objects.all().annotate(posts_count=Count('post'))
    tags = BlogTag.objects.all()

    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name=kwargs["cat_name"])

    if kwargs.get("tag_name") != None:
        posts = posts.filter(tag__name=kwargs["tag_name"])

    posts = Paginator(posts, 8)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {"posts": posts, "categories": categories, "last_posts": last_posts, "tags": tags}
    return render(request, 'blog/blog_home_page.html', context)


def blog_single_view(request):
    return render(request, 'blog/blog_single_page.html')