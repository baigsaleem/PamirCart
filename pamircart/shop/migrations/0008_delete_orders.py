# Generated by Django 4.0.3 on 2022-03-14 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
