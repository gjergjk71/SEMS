# Generated by Django 2.0.4 on 2018-06-18 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0011_provimet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provimet',
            name='times',
        ),
    ]
