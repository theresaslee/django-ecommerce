from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    """When you go to url, takes request and returns response."""
    return render(request, "home_page.html", {})
