# Generated by Django 4.1.2 on 2022-10-24 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0003_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='transcation_id',
            new_name='transaction_id',
        ),
    ]