from django.shortcuts import render


def home(request):
    return render(request, "path/home.html")


def about_me(request):
    return render(request, "path/about.html")
