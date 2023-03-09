from django.template import Library

from utils import utils

register = Library()


@register.filter
def format_price(val):
    return utils.format_price(val)


@register.filter
def cart_total_qt(cart):
    return utils.cart_total_qt(cart)

@register.filter
def total_cart(cart):
    return utils.total_cart(cart)
