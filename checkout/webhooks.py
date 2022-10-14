from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import stripe
import django_store.settings as settings
from checkout import models
from store.models import Order, Product


@csrf_exempt
def stripe_webhook(request):
    print('Stripe Webhook')
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
        )
    except ValueError as e:
        print('Invalid payload')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print('Invalid signature')
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        print('payment_intent.succeeded')
        print(payment_intent.metadata)
        transaction_id = payment_intent.metadata.transaction
        make_order(transaction_id)
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event['type']))
    return HttpResponse(status=200)



def make_order(transaction_id):
    transaction = models.Transaction.objects.get(pk=transaction_id)
    order = Order.objects.create(transaction=transaction)
    products = Product.objects.filter(pk__in=transaction.items)
    for product in products:
        order.ordersproduct_set.create(product_id=product.id, price=product.price)

    msg_html = render_to_string('emails/order.html', {
        'order': order,
        'products': products
    })
    send_mail(
        subject='New Order',
        html_message=msg_html,
        message=msg_html,
        from_email='noreplay@bookstore.com',
        recipient_list=[order.transaction.customer_email]
    )