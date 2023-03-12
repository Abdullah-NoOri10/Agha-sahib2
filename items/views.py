from django.shortcuts import render
from .models import Product, Companie

# Create your views here.


def comps(request):
    names = Companie.objects.only('name')
    context = {'names': names}

    return render(request, 'home.html', context)
