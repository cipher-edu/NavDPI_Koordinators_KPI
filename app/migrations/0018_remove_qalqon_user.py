# Generated by Django 4.2.6 on 2024-01-03 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_qalqon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qalqon',
            name='user',
        ),
    ]