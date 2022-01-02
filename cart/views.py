from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


def cart(request, tot=0, count=0, cart_items=None):
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
        ct_items = Item.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prdt.price * i.quan)
            count += i.quan
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = Product.objects.get(id=product_id)
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
    except Cartlist.DoesNotExist:
        ct = Cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = Item.objects.get(prdt=prod, cart=ct)
        if c_items.quan < c_items.prdt.stock:
            c_items.quan += 1
        c_items.save()
    except Item.DoesNotExist:
        c_items = Item.objects.create(prdt=prod, quan=1, cart=ct)
        c_items.save()
    return redirect('cart')


def min_cart(request, product_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Product, id=product_id)
    c_items = Item.objects.get(prdt=prod, cart=ct)
    if c_items.quan > 1:
        c_items.quan -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart')


def delete(request, product_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Product, id=product_id)
    c_items = Item.objects.get(prdt=prod, cart=ct)
    c_items.delete()
    return redirect('cart')

# Create your views here.
