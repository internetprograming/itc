# Generated by Django 2.2.1 on 2019-05-25 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
