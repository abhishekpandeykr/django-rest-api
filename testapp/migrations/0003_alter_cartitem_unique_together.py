# Generated by Django 4.0.3 on 2022-03-10 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_slug'),
        ('testapp', '0002_cart_cartitem'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]
