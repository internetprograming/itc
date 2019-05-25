from django.conf.urls import url


from .views import (
    order_details
)

urlpatterns = [
    url('order_summary', order_details, name="order_summary"),
]