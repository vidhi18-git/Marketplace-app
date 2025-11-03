from django.shortcuts import render,get_object_or_404,reverse
from .models import Product,OrderDetail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe , json
from django.http import JsonResponse,HttpResponseNotFound
#------------------ Home Page (index view) -------------------#

def index(request):
    products = Product.objects.all()
    return render(request,'myapp/index.html',{'products':products})

#-------------- Detail Page View --------------------#
def detail(request,id):
    product = Product.objects.get(id=id)
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request,'myapp/detail.html',{'product':product,'stripe_publishable_key':stripe_publishable_key})

#----------------checkout session creation view--------------#
@csrf_exempt
def create_checkout_session(request, id):
    request_data = json.loads(request.body)
    product = Product.objects.get(id=id)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        customer_email=request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    order = OrderDetail()
    order.customer_email = request_data['email']
    order.product = product
    order.stripe_payment_intent = checkout_session.payment_intent   # keep this
    order.stripe_session_id = checkout_session.id                   # ✅ add THIS
    order.price = int(product.price)                                # ✅ fix wrong field
    order.save()

    return JsonResponse({'sessionId': checkout_session.id})

def payment_success_view(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return HttpResponseNotFound()

    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.retrieve(session_id)

    # ✅ match using session_id, not payment_intent
    order = get_object_or_404(OrderDetail, stripe_session_id=session_id)

    order.has_paid = True
    order.save()

    return render(request, 'myapp/payment_success.html', {'order': order})



        
def payment_failed(request):
    return render(request,'myapp/payment_failed.html')
