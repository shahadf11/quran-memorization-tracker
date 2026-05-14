from django.shortcuts import render


def home(request):
    return render(request, 'tracker/home.html')


def surahs(request):
    return render(request, 'tracker/surahs.html')


def progress(request):
    return render(request, 'tracker/progress.html')


def add_entry(request):
    return render(request, 'tracker/add_entry.html')