from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, User
from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.utils import timezone
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
    user = models.OneToOneField(User,on_delete=models.CASCADE )
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
    
    def send_task_to_coordinators(self, task_name, task_body, task_duration_hours, coordinators=None):
        current_time = timezone.now()
        end_time = current_time + timezone.timedelta(hours=task_duration_hours)

        task = Task.objects.create(
            task_name=task_name,
            task_body=task_body,
            task_date=current_time,
            task_and_date=end_time
        )

        if coordinators:
            task.coordinators.add(*coordinators)  # Add the specified coordinators to the task

    def __str__(self):
        return self.name

class Task(models.Model):
    task_name = models.CharField(max_length=25, verbose_name='Topshiriq nomi')
    task_body = models.TextField(verbose_name='Topshiriq Mazmuni')
    task_date = models.DateTimeField(auto_now=False, verbose_name='Topshiriq yuklangan vaqt')
    task_and_date = models.DateTimeField(auto_now=False, verbose_name='Topshiriq tugash vaqti')
    coordinators = models.ManyToManyField(Kordinators, blank=True, verbose_name='Assigned Coordinators')
    task_file = models.FileField(upload_to='topshiriqlar/', null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.task_name