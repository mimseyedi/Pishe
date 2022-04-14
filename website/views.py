from django.shortcuts import render
from django.contrib import messages
from website.forms import ContactForm
from blog.models import Post


def home_view(request):
    posts = Post.objects.filter(status=1)
    last_posts = posts[:3]
    context = {"last_posts": last_posts}
    return render(request, 'website/home_page.html', context)


def about_view(request):
    return render(request, 'website/aboutus_page.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'نظر شما با موفقیت ثبت شد!')
        else:
            messages.add_message(request, messages.ERROR, 'متاسفانه نظر شما ثبت نشد!')

    form = ContactForm()
    return render(request, 'website/contact_page.html', {"form": form})
