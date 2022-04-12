from django.urls import path

from payment.views import Checkout,paymenthandler
urlpatterns = [
    path('checkout/',Checkout.as_view(),name='checkout'),
    path('checkout/paymenthandler/',paymenthandler,name='paymenthandler'),

]