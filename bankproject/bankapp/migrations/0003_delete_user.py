# Generated by Django 4.1.2 on 2022-10-08 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
