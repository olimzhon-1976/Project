# Generated by Django 4.2.7 on 2024-08-18 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_alter_cart_created_timestamp_alter_cart_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('id',), 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
    ]
