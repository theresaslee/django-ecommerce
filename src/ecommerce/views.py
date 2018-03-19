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
        "title": "Contact Page!",
        "content": "Welcome to the contact page."
    }

    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))

    return render(request, "contact/view.html", context)
