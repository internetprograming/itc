from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import OrderItem , Order
from django.conf import settings

def get_user_pending_order(request):
    # get order for the correct user
    #user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=settings.AUTH_USER_MODE, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)