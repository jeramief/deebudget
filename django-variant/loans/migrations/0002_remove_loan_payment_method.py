# Generated by Django 5.1 on 2025-03-21 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='payment_method',
        ),
    ]
