# Generated by Django 2.0.4 on 2018-06-21 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0015_provimet_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provimet',
            name='status',
        ),
    ]
