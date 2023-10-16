from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
def validate_image_size(value):
    limit = 2 * 1024 * 1024  # 2 MB in bytes
    if value.size > limit:
        raise ValidationError('File size too large. Max size is 2 MB.')

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
    image = models.ImageField(upload_to='media/Kordinator_logo/', validators=[validate_image_size])
    about = models.TextField(verbose_name='O\'zi haqida')
    telegram = models.CharField(max_length=250, verbose_name='Telegram link')
    mail = models.CharField(max_length=250, verbose_name='Mail')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='media/post_images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def image_tag(self):
        return format_html('<img src="{}" style="height: 100px;" />', self.image.url)

    image_tag.short_description = 'Image'

class Posts(models.Model):
    post_title = models.CharField(max_length=255, verbose_name='Post sarlavhasi')
    post_content = models.TextField(verbose_name='Post content')
    category = models.ForeignKey('Kordinators', on_delete=models.CASCADE, verbose_name='Post kordinatori')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(choices=author, max_length=255, verbose_name='Author')
    images = models.ManyToManyField(Image, blank=True, verbose_name='Post Images')

    def display_images(self):
        return format_html(''.join(image.image_tag() for image in self.images.all()))

    display_images.short_description = 'Images'

    def get_image_views(self):
        return format_html(''.join(image.image_tag() for image in self.images.all()))

    get_image_views.short_description = 'Image Views'

    def __str__(self):
        return self.post_title
