# Generated by Django 4.1.2 on 2022-10-08 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='item',
            new_name='items',
        ),
    ]
