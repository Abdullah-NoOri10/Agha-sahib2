from django.shortcuts import render, redirect
from .models import Product, Companie, User
from .forms import CreateProductForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout

# Create your views here.


def comps(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        names = Companie.objects.only('name')
        context = {'names': names}
        return render(request, 'home.html', context)


def profile(request, pk):
    company = Companie.objects.get(id=pk)
    products = company.product_set.all()
    context = {'company': company, 'products': products}
    return render(request, 'profile.html', context)


def create_product(request):
    form = CreateProductForm

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        product = request.POST.get('product')

        product = Product.objects.create(

        )

    return render(request, 'createproduct.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_user(request, user)
            return redirect('companies')
        else:
            return redirect('error')

    context = {}
    return render(request, 'login.html', context)


def error_page(request):
    context = {}
    return render(request, 'error.html', context)
