from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models

# Create your views here.


class ListProducts(ListView):
    model = models.Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 10


class DetailProduct(DetailView):
    model = models.Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddToCart(View):
    def get(self, *args, **kwargs):

        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('product:list'))
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(
                self.request,
                'Product doesnt exists.'
            )
            return redirect(http_referer)

        variation = get_object_or_404(models.Variation, id=variation_id)
        variation_stock = variation.stock
        product = variation.product

        product_id = product.id  # type: ignore
        product_name = product.name
        variation_name = variation.name or ''
        unit_price = variation.price
        unit_promotional_price = variation.promotional_price
        quantity = 1
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.stock < 1:
            messages.error(
                self.request,
                'Insufficient stock.'
            )
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()

        cart = self.request.session['cart']

        if variation_id in cart:
            quantity_cart = cart[variation_id]['quantity']
            quantity_cart += 1

            if variation_stock < quantity_cart:
                messages.warning(
                    self.request,
                    f'Insufficient stock to {quantity_cart}x on the product {product.name}. We added {variation_stock}x on your cart.'
                )
                quantity_cart = variation_stock

            cart[variation_id]['quantity'] = quantity_cart
            cart[variation_id]['quantitative_price'] = unit_price * quantity_cart
            cart[variation_id]['quantitative_promotional_price'] = unit_promotional_price * quantity_cart

        else:
            cart[variation_id] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_name': variation_name,
                'variation_id': variation_id,
                'unit_price': unit_price,
                'unit_promotional_price': unit_promotional_price,
                'quantitative_price': unit_price,
                'quantitative_promotional_price': unit_promotional_price,
                'quantity': 1,
                'slug': slug,
                'image': image,
            }

        self.request.session.save()
        messages.success(self.request,
                         f'Product {product_name} - {variation_name} added to your cart {cart[variation_id]["quantity"]}x')  # type:ignore
        return redirect(http_referer)


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('product:list'))
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            return redirect(http_referer)
        
        if not self.request.session.get('cart'):
            return redirect(http_referer)
        
        if variation_id not in self.request.session['cart']:
            return redirect(http_referer)
        
        cart = self.request.session['cart'][variation_id]

        messages.success(
            self.request,
            f'Product{cart["product_name"]} {cart["variation_name"]} removed of your cart.'
        )

        del self.request.session['cart'][variation_id]
        self.request.session.save()

        return redirect(http_referer)


class Cart(View):
    def get(self, *args, **kwargs):
        context = {
            'cart': self.request.session.get('cart', {})
        }
        return render(self.request, 'product/cart.html', context)


class PurshaseSummary(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalize')
