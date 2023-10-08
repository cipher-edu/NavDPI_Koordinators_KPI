# Generated by Django 4.2.6 on 2023-10-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_kordinators_fak_alter_kordinators_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kordinators',
            name='ilimiy_darajasi',
            field=models.CharField(choices=[('Tugallanmangan bakalavr', 'Tugallanmangan bakalavr'), ('Magister', 'Magister')], default=1, max_length=25, verbose_name='Ilmiy unvoni'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kordinators',
            name='image',
            field=models.ImageField(default=1, upload_to='media/Kordinator_logo/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kordinators',
            name='kor_lavozimi',
            field=models.CharField(choices=[('Metematika', 'Matematika'), ('Fizika', 'Fizika'), ("Sana'tshunoslik", "Sana'tshunoslik"), ('Jismoniy madaniyat', 'Jismoniy madaniyat'), ('Tabiy fanlar', 'Tabiy fanlar'), ('Ingliz tili va adabiyoti', 'Ingliz tili va adabiyoti'), ('Rus tili va Qozoq tillari filialogiyasi', 'Rus tili va Qozoq tillari filialogiyasi'), ('Tibbiyot', 'Tibbiyot'), ("Maktabgacha va boshlang'ich ta'lim", "Maktabgacha va boshlang'ich ta'lim"), ('Tarix', 'Tarix'), ('O‘zbek tili va adabiyoti fakulteti', 'O‘zbek tili va adabiyoti fakulteti'), ('Tadbirkorlik va innovatsion loyihalar koordinatori', 'Tadbirkorlik va innovatsion loyihalar koordinatori'), ('Intellektual loyihalar koordinatori', 'Intellektual loyihalar koordinatori'), ('Besh tashabbus loyihalar koordinatori', 'Besh tashabbus loyihalar koordinatori'), ('Harbiy-vatanparvarlik loyihalar koordinatori', 'Harbiy-vatanparvarlik loyihalar koordinatori'), ('Yoshlar daftari va metsenatlik dasturlari koordinatori', 'Yoshlar daftari va metsenatlik dasturlari koordinatori'), ('Talaba qizlar koordinatori', 'Talaba qizlar koordinatori'), ('Matbuot kotibi, media guruh rahbari', 'Matbuot kotibi, media guruh rahbari')], default=1, max_length=255, verbose_name='Kordinatorligi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kordinators',
            name='tel',
            field=models.IntegerField(default=1, verbose_name='Telefon raqami'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kordinators',
            name='fak',
            field=models.CharField(choices=[('Metematika', 'Matematika'), ('Fizika', 'Fizika'), ("Sana'tshunoslik", "Sana'tshunoslik"), ('Jismoniy madaniyat', 'Jismoniy madaniyat'), ('Tabiy fanlar', 'Tabiy fanlar'), ('Ingliz tili va adabiyoti', 'Ingliz tili va adabiyoti'), ('Rus tili va Qozoq tillari filialogiyasi', 'Rus tili va Qozoq tillari filialogiyasi'), ('Tibbiyot', 'Tibbiyot'), ("Maktabgacha va boshlang'ich ta'lim", "Maktabgacha va boshlang'ich ta'lim"), ('Tarix', 'Tarix'), ('O‘zbek tili va adabiyoti fakulteti', 'O‘zbek tili va adabiyoti fakulteti')], default=None, max_length=155, verbose_name='Fakulteti'),
        ),
    ]
