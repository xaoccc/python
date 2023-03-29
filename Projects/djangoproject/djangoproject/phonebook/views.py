from django.shortcuts import render, redirect


def landing_page(request):
    return render(request, "phonebook/index.html")
