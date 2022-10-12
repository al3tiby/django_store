from django.db import models
from django.utils.translation import gettext as ___



class TransactionStatus(models.IntegerChoices):
    Pending = 0, ___('Pending')
    Completed = 1, ___('Completed')


class PaymentMethod(models.Model):
    Stripe = 1, ___('Stripe')
    Paypal = 2, ___('PayPal')





class Transaction(models.Model):
    session = models.CharField(max_length=255)
    amount = models.FloatField()
    items = models.JSONField(default=dict)
    customer = models.JSONField(default=dict)
    status = models.IntegerField(
        choices=TransactionStatus.choices, default=TransactionStatus.Pending
    )
    payment_method = models.IntegerField(
        choices=TransactionStatus.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def customer_name(self):
        return self.customer['first_name'] + ' ' + self.customer['last_name']

    @property
    def customer_email(self):
        return self.customer['email']