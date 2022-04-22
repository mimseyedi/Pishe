from django.shortcuts import render


def bookstore_home_view(request):
    return render(request, "bookstore/bookstore_home.html")
