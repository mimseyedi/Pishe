from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bookstore.models import BookComment, BookStoreCategory, Book
from django.contrib import messages
from bookstore.forms import BookCommentForm
from account.models import ProductFavorite


def bookstore_home_view(request, **kwargs):
    books = Book.objects.all()
    last_books = books[:4]
    categories = BookStoreCategory.objects.all().annotate(posts_count=Count('book'))

    if request.method == "GET":
        if s := request.GET.get('s'):
            books = books.filter(title__contains=s)

    if kwargs.get("cat_name") != None:
        books = books.filter(category__name=kwargs["cat_name"])

    books = Paginator(books, 15)
    try:
        page_number = request.GET.get('page')
        books = books.get_page(page_number)
    except PageNotAnInteger:
        books = books.get_page(1)
    except EmptyPage:
        books = books.get_page(1)

    context = {"books": books, "categories": categories, "last_books": books}
    return render(request, "bookstore/bookstore_home.html", context)


def bookstore_single_view(request, book_id, **kwargs):
    products_fav = ProductFavorite.objects.filter(user=request.user.pk)
    book_exists_in_fav = ProductFavorite.objects.filter(user=request.user.pk, book=book_id)
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        if "comment_submit" in request.POST:
            form = BookCommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'نظر شما با موفقیت ثبت شد! بعد از تایید در صفحه درج خواهد شد.')
            else:
                messages.add_message(request, messages.ERROR, 'متاسفانه نظر شما ثبت نشد!')

        elif "unfav_submit" in request.POST:
            this_book = ProductFavorite.objects.filter(user=request.user.pk, book=book_id)
            this_book.delete()

        elif "fav_submit" in request.POST:
            new_fav_book = ProductFavorite()
            new_fav_book.user = request.user
            new_fav_book.book = book
            new_fav_book.save()


    books = Book.objects.all()
    last_books = books[:6]
    comments = BookComment.objects.filter(book=book.id, approved=True).order_by('-created_date')

    context = {"book": book, "last_books": last_books, "comments": comments, "products_fav": products_fav,
               "book_exists_in_fav": book_exists_in_fav}
    return render(request, "bookstore/bookstore_single.html", context)


def checkout_view(request):
    return render(request, "bookstore/bookstore_checkouts.html")


def cart_view(request):

    return render(request, "bookstore/bookstore_cart.html")