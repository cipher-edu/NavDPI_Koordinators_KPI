# Generated by Django 4.2.6 on 2023-10-18 17:06

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0006_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kordinators',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='kordinators',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='kordinators',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='kordinators', to='auth.group', verbose_name='Groups'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='Parol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kordinators',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='kordinators_user_permissions', to='auth.permission', verbose_name='User Permissions'),
        ),
        migrations.AddField(
            model_name='kordinators',
            name='username',
            field=models.CharField(default=1, max_length=30, unique=True, verbose_name='Login'),
            preserve_default=False,
        ),
    ]