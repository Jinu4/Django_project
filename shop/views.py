from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def fun(request):
    ob1 = Category.objects.all()
    ob2 = Product.objects.all()
    return render(request, 'index.html', {'c': ob1, 'p': ob2})


def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod})


def cate(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        prodt = Product.objects.filter(category=c_page, available=True)
    else:
        prodt = Product.objects.all().filter(available=True)
    paginator = Paginator(prodt, 2)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'gallery.html', {'p': prodt, 'pg': pro})


def details(request, c_slug, product_slug):
    try:
        prod = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop-detail.html', {'p': prod})

# Create your views here.
