from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post, BlogCategory, BlogTag, Comment
from blog.forms import CommentForm
from django.contrib import messages


def blog_home_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    last_posts = posts[:3]
    categories = BlogCategory.objects.all().annotate(posts_count=Count('post'))
    tags = BlogTag.objects.all()

    if request.method == "GET":
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name=kwargs["cat_name"])

    if kwargs.get("tag_name") != None:
        posts = posts.filter(tag__name=kwargs["tag_name"])

    posts = Paginator(posts, 6)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {"posts": posts, "categories": categories, "last_posts": last_posts, "tags": tags}
    return render(request, 'blog/blog_home_page.html', context)


def blog_single_view(request, post_id, **kwargs):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'نظر شما با موفقیت ثبت شد! بعد از تایید در صفحه درج خواهد شد.')
        else:
            messages.add_message(request, messages.ERROR, 'متاسفانه نظر شما ثبت نشد!')


    post = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.filter(status=1)
    end_last_posts = posts[:2]
    last_posts = posts[:3]

    categories = BlogCategory.objects.all().annotate(posts_count=Count('post'))
    tags = BlogTag.objects.all()
    comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')


    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name=kwargs["cat_name"])

    if kwargs.get("tag_name") != None:
        posts = posts.filter(tag__name=kwargs["tag_name"])

    context = context = {"posts": posts, "post": post, "categories": categories, "end_last_posts": end_last_posts,
                         "last_posts": last_posts, "tags": tags, 'comments': comments}

    return render(request, 'blog/blog_single_page.html', context)
