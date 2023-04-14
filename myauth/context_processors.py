from myauth.models import Cart
from django.db.models import Sum
from django.http import JsonResponse

def cart_total_qty(request):
    if request.user.is_authenticated:
        total_qty = Cart.objects.filter(user=request.user.id).aggregate(Sum('product_qty'))['product_qty__sum'] or 0
    else:
        total_qty = 0
    return {'total_qty': total_qty}