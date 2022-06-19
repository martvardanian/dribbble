from django.shortcuts import render
from .models import Cards


def index(request):
    cards = Cards.objects.all()
    return render(request, 'blog/index.html', { "cards": cards})


def contact(request):
    return render(request, 'static/contact.html')


def about(request):
    return render(request, 'static/about.html')
