# Generated by Django 3.0.7 on 2020-07-23 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='extra_field',
        ),
    ]
