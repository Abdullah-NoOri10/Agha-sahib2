from django.shortcuts import render
from .models import Product, Companie, User
from .forms import ProductForm

# Create your views here.


def comps(request):
    names = Companie.objects.only('name')
    context = {'names': names}
    return render(request, 'home.html', context)


def profile(request, pk):
    company = Companie.objects.get(id=pk)
    products = company.product_set.all()
    context = {'company': company, 'products': products}
    return render(request, 'profile.html', context)


def newform(request):
    form = ProductForm

    return render(request, 'new.html', {'form': form})
