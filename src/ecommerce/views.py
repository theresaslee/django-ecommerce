from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    """When you go to url, takes request and returns response."""
    context = {
        "title": "Hello World!",
        "content": "Welcome to the home page"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    """When you go to url, takes request and returns response."""
    context = {
        "title": "About Page!"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    """When you go to url, takes request and returns response."""
    context = {
        "title": "Contact Page!"
    }
    return render(request, "home_page.html", context)
