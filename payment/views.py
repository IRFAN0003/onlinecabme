
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic import View
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
)

class Checkout(View):
    template_name = 'payment/checkout.html'
    def get(self, request):
        currency = 'INR'
        amount = self.request.GET.get('amount')
        
        print(amount)

        razorpay_order = razorpay_client.order.create(
            dict(amount=amount,currency=currency, payment_capture='0')
            )
        
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler/'

        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
 
        return render(request, self.template_name, context=context)

    def post(self, request):
        pass


@csrf_exempt
def paymenthandler(request):
    if request.method == 'POST':
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'payment/paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'payment/paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'payment/paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()