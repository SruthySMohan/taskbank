# Generated by Django 4.1.2 on 2022-10-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('Password', models.TextField()),
                ('Password1', models.TextField()),
            ],
        ),
    ]
