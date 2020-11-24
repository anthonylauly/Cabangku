from django import template
import numpy as np

register = template.Library()

@register.simple_tag
def total_shops(shops):
    return len(shops)

def shop_columns(shops, n):
    try:
        n = int(n)
        shops = list(shops)
    except (ValueError, TypeError):
        return [shops]
    shop_len = len(shops)
    split = int(np.ceil(shop_len/n))
    return [shops[i*split:(i+1)*split] for i in range(split)]

register.filter('columns', shop_columns)