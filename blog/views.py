from django.shortcuts import render
from .models import Cards


def index(request):
    cards = Cards.objects.filter(is_published=True).order_by('created_at')[::-1]
    return render(request, 'blog/index.html', {"cards": cards})


def contact(request):
    return render(request, 'static/contact.html')


def about(request):
    return render(request, 'static/about.html')


def post(request, id):
    card = Cards.objects.get(id=id)
    return render(request, 'blog/full.html', {"card": card})
