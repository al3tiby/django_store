from django.db import models
from django.utils.translation import gettext as ___


class OrderReport(models.Model):
    class Meta:
        verbose_name_plural = ___('Orders')