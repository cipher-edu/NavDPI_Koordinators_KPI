# Generated by Django 4.2.6 on 2024-01-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_qalqon_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qalqon',
            name='all_stat_file',
            field=models.FileField(blank=True, null=True, upload_to='beshtashabbus/', verbose_name="Faylni briktiring mavjud bo'lsa"),
        ),
    ]