def format_price(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qt(cart):
    return sum([item['quantity'] for item in cart.values()])

def total_cart(cart):
    return sum(
        [
            item.get('quantitative_promotional_price') 
            if item.get('quantitative_promotional_price') 
            else item.get('quantitative_price') for item in cart.values()
        ]
    )