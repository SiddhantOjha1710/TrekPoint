# Generated by Django 4.1.2 on 2022-10-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upcoming', '0003_alter_treks_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='treks',
            name='digital',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
