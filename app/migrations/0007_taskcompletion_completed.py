# Generated by Django 4.2.6 on 2023-10-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcompletion',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Task Completed'),
        ),
    ]