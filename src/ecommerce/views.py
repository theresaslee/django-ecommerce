from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm


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
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page!",
        "content": "Welcome to the contact page.",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)
