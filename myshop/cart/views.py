from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from myshop.shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(
            product=product,
            quantity=cleaned_data['quantity'],
            override_quantity=cleaned_data['override']
        )
    return redirect('cart:cart_detail')
