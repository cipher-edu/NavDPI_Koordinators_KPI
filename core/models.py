from django.db import models
import uuid
# Create your models here.

fakultets = [
        ('Metematika', 'Matematika'),
        ('Fizika', 'Fizika'),
        ('Sana\'tshunoslik','Sana\'tshunoslik'),
        ('Jismoniy madaniyat','Jismoniy madaniyat'),
        ('Tabiy fanlar', 'Tabiy fanlar'),
        ('Ingliz tili va adabiyoti','Ingliz tili va adabiyoti'),
        ('Rus tili va Qozoq tillari filialogiyasi', 'Rus tili va Qozoq tillari filialogiyasi'),
        ('Tibbiyot','Tibbiyot'),
        ('Maktabgacha va boshlang\'ich ta\'lim','Maktabgacha va boshlang\'ich ta\'lim'),
        ('Tarix', 'Tarix'),
        ('O‘zbek tili va adabiyoti fakulteti', 'O‘zbek tili va adabiyoti fakulteti'),

    ]
kordinator_states = [
        ('Metematika', 'Matematika'),
        ('Fizika', 'Fizika'),
        ('Sana\'tshunoslik','Sana\'tshunoslik'),
        ('Jismoniy madaniyat','Jismoniy madaniyat'),
        ('Tabiy fanlar', 'Tabiy fanlar'),
        ('Ingliz tili va adabiyoti','Ingliz tili va adabiyoti'),
        ('Rus tili va Qozoq tillari filialogiyasi', 'Rus tili va Qozoq tillari filialogiyasi'),
        ('Tibbiyot','Tibbiyot'),
        ('Maktabgacha va boshlang\'ich ta\'lim','Maktabgacha va boshlang\'ich ta\'lim'),
        ('Tarix', 'Tarix'),
        ('O‘zbek tili va adabiyoti fakulteti', 'O‘zbek tili va adabiyoti fakulteti'),
        ('Tadbirkorlik va innovatsion loyihalar koordinatori', 'Tadbirkorlik va innovatsion loyihalar koordinatori'),
        ('Intellektual loyihalar koordinatori','Intellektual loyihalar koordinatori'),
        ('Besh tashabbus loyihalar koordinatori','Besh tashabbus loyihalar koordinatori'),
        ('Harbiy-vatanparvarlik loyihalar koordinatori', 'Harbiy-vatanparvarlik loyihalar koordinatori'),
        ('Yoshlar daftari va metsenatlik dasturlari koordinatori', 'Yoshlar daftari va metsenatlik dasturlari koordinatori'),
        ('Talaba qizlar koordinatori', 'Talaba qizlar koordinatori'),
        ('Matbuot kotibi, media guruh rahbari','Matbuot kotibi, media guruh rahbari')
]
ilmiy_daraja = [
    ('Tugallanmangan bakalavr', 'Tugallanmangan bakalavr'),
    ('Magister', 'Magister')
]
author = [
    ('Matbuot kotibi', 'Matbuot kotibi'),
    ('Admin', 'Admin')
]
class Kordinators(models.Model):
    name = models.CharField(max_length=25, verbose_name='Ismi')
    lastname = models.CharField(max_length=25, verbose_name='Familiyasi')
    surname = models.CharField(max_length=25, verbose_name='Otasining ismi')
    age = models.IntegerField(verbose_name='Yoshi')
    fak = models.CharField(max_length=155, choices=fakultets, default=None, verbose_name='Fakulteti')
    ilimiy_darajasi = models.CharField(max_length=25, choices=ilmiy_daraja, verbose_name='Ma\'lumoti')
    kor_lavozimi = models.CharField(max_length=255, choices=kordinator_states, verbose_name='Kordinatorligi')
    tel = models.IntegerField(verbose_name='Telefon raqami')
    image = models.ImageField(upload_to='media/Kordinator_logo/')
    about = models.TextField(verbose_name='O\'zi haqida')
    telegram = models.CharField(max_length=250, verbose_name='Telegram link')
    mail = models.CharField(max_length=250, verbose_name='Mail')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.name


class Posts(models.Model):
    # Allow multiple photos by using a ManyToMany relationship
    photos = models.ManyToManyField('PostPhoto', related_name='posts', blank=True)
    post_title = models.CharField(max_length=255, verbose_name='Post sarlavhasi')
    post_content = models.TextField(verbose_name='Post content')
    category = models.ForeignKey('Kordinators', on_delete=models.CASCADE, verbose_name='Post kordinatori')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(choices=author, max_length=255, verbose_name='Author')
    def __str__(self):
        return self.post_title

    photos = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return self.post_title

class Image(models.Model):
    image = models.ImageField(upload_to='media/post_images/')