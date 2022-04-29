from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bookstore.models import BookComment, BookStoreCategory, Book, Cart, Product, Order, OrderProduct
from django.contrib import messages
from bookstore.forms import BookCommentForm
from account.models import UserInfo
from account.models import ProductFavorite
from django.urls import reverse
from random import randint


def bookstore_home_view(request, **kwargs):
    books = Book.objects.all()
    last_books = books[:5]
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

    context = {"books": books, "categories": categories, "last_books": last_books}
    return render(request, "bookstore/bookstore_home.html", context)


def bookstore_single_view(request, book_id, **kwargs):
    products_fav = ProductFavorite.objects.filter(user=request.user.pk)
    book_exists_in_fav = ProductFavorite.objects.filter(user=request.user.pk, book=book_id)
    book = get_object_or_404(Book, pk=book_id)
    cart = Cart.objects.filter(user=request.user)

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

        elif "add_to_cart_submit" in request.POST:
            if not Product.objects.filter(book=book):
                new_prod = Product.objects.create(book=book, count=request.POST.get("count"))
                user_cart = Cart.objects.get(user=request.user)
                user_cart.product.add(new_prod)
                total_p = 0
                for product in user_cart.product.all():
                    total_p += product.book.price * product.count
                user_cart.total_price = total_p
                user_cart.save()
            else:
                user_cart = Cart.objects.get(user=request.user)
                total_p = 0
                pr = Product.objects.get(book=book)
                c = request.POST.get("count")
                pr.count += int(c)
                pr.save()
                user_cart.product.add(pr)
                for product in user_cart.product.all():
                    total_p += product.book.price * product.count
                user_cart.total_price = total_p
                user_cart.save()

    books = Book.objects.all()
    last_books = books[:6]
    comments = BookComment.objects.filter(book=book.id, approved=True).order_by('-created_date')

    context = {"book": book, "last_books": last_books, "comments": comments, "products_fav": products_fav,
               "book_exists_in_fav": book_exists_in_fav, "cart": cart}
    return render(request, "bookstore/bookstore_single.html", context)


def checkout_view(request):
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        user_cart = Cart.objects.get(user=request.user)

        if request.method == "POST":
            products = Product.objects.all()
            for p in products:
                check_p = OrderProduct.objects.filter(book=p.book, count=p.count)
                if not check_p:
                    prod = OrderProduct.objects.create(book=p.book, count=p.count)

            order = Order()
            order.user = request.user
            order.total_price = user_cart.total_price
            order.order_id = randint(10000, 100000)
            order.save()

            user_order = Order.objects.get(order_id=order.order_id)

            for p in products:
                order_prod = OrderProduct.objects.get(book=p.book, count=p.count)
                user_order.product.add(order_prod)

            products = Product.objects.all()
            products.delete()

            user_cart.total_price = 0
            user_cart.save()

            return HttpResponseRedirect(reverse("suc_paid"))

        context = {"user": user_info, "user_cart": user_cart}
        return render(request, "bookstore/bookstore_checkouts.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def cart_view(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.get(user=request.user)

        if request.method == "POST":
            if "update_submit" in request.POST:
                for product in user_cart.product.all():
                    if product.count != int(request.POST.get(f"product_count{product.pk}")):
                        product.count = int(request.POST.get(f"product_count{product.pk}"))
                        product.save()

                total_p = 0
                for product in user_cart.product.all():
                    total_p += product.book.price * product.count
                user_cart.total_price = total_p
                user_cart.save()

            elif "del_submit" in request.POST:
                product = Product.objects.get(pk=int(request.POST.get("product_pk")))
                product.delete()
                total_p = 0
                for product in user_cart.product.all():
                    total_p += product.book.price * product.count
                user_cart.total_price = total_p
                user_cart.save()
                return HttpResponseRedirect(reverse("cart"))
    else:
        return HttpResponseRedirect(reverse("login"))

    context = {"user_cart": user_cart}
    return render(request, "bookstore/bookstore_cart.html", context)


def suc_paid_view(request):
    if request.user.is_authenticated:
        return render(request, "bookstore/bookstore_pay_accepted.html")
    else:
        return HttpResponseRedirect(reverse("login"))
