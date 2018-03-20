from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm


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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to success page
            return redirect('/login')
        else:
            print('Error')
    return render(request, "auth/login.html", context)

def register_page(request):
    return render(request, "auth/register.html", {})
