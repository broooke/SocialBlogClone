# Generated by Django 3.1.5 on 2021-01-11 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20210111_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
