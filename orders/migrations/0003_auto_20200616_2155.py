# Generated by Django 2.0.3 on 2020-06-16 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order2_order_counter_user_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subs',
            new_name='Sub',
        ),
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]