
from django.contrib import admin
from django.urls import path
from . import views, webhooks

urlpatterns = [
    path('stripe/config', webhooks.stripe_webhook, name='checkout.stripe.config'),
    path('stripe/webhook', views.stripe_config),
    path('stripe', views.stripe_transaction, name='checkout.stripe'),
    path('paypal', views.stripe_transaction, name='checkout.paypal')
]
