from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, User
from django.db import models
import uuid
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
def validate_image_size(value):
    limit = 2 * 1024 * 1024  # 2 MB in bytes
    if value.size > limit:
        raise ValidationError('File size too large. Max size is 2 MB.')
besh_tashabbus = [
    ('Yosh kitobxon', 'Yosh kitobxon'),
    ('Quvnoqlar va zukkolar', 'Quvnoqlar va zukkolar'),
    
]

intelektual = [
    ('Talabalar ligasi','Talabalar ligasi'),
    ('Intellektual liga', 'Intellektual liga'),
    ('Rektor kubogi','Rektor kubogi'),
    ('Breyn Ring','Breyn Ring'),
    ('Zakovat Quiz','Zakovat Quiz'),
    ("Shaxsiy o'yin", "Shaxsiy o'yin")
]
fakultets = [
        ('Metematika - Informatika', 'Matematika - Informatika'),
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
        ('Metematika - Informatika', 'Matematika - Informatika '),
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
    ('Bakalavr', 'Bakalavr'),
    ('Magistr', 'Magistr')
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
    image = models.ImageField(upload_to='Kordinator_logo/', validators=[validate_image_size])
    about = models.TextField(verbose_name='O\'zi haqida')
    telegram = models.CharField(max_length=250, verbose_name='Telegram link')
    mail = models.CharField(max_length=250, verbose_name='Mail')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    @classmethod
    def total_koordinator(cls):
        return cls.objects.count()
    
    def __str__(self):

        return self.user.name

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
            for coordinator in coordinators:
                task.coordinators.add(coordinator) 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Koordinatorlar'
        verbose_name_plural = 'Koordinatorlar ro\'yxati'

class Task(models.Model):
    task_name = models.CharField(max_length=255, verbose_name='Topshiriq nomi')
    task_body = models.TextField(verbose_name='Topshiriq Mazmuni')
    task_date = models.DateTimeField(auto_now=False, verbose_name='Topshiriq yuklangan vaqt')
    task_and_date = models.DateTimeField(auto_now=False, verbose_name='Topshiriq tugash vaqti')
    coordinators = models.ManyToManyField(Kordinators, blank=True, verbose_name='Koordinatorlani tanlash')
    task_file = models.FileField(upload_to='topshiriqlar/', null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #received_by = models.ManyToManyField(Kordinators, blank=True, related_name='received_tasks', verbose_name='Received by Coordinators')
    completed = models.BooleanField(default=False, null=True,verbose_name='vazifalalrning qabul qilinish holati')
    
    @classmethod
    def total_tasks(cls):
        return cls.objects.count()
    
    @classmethod
    def completed_tasks_count(cls):
        return cls.objects.filter(completed=True).count()
    
    @classmethod
    def nocompleted_tasks_count(cls):
        return cls.objects.filter(completed=False).count()
    
    def mark_as_received(self, coordinator):
            """
            Marks the task as received by a coordinator.
            """
            if coordinator not in self.coordinators.all():
                return

            if coordinator not in self.received_by.all():
                self.received_by.add(coordinator)
                
                self.completed = True
                self.save()
        
    # def is_received_by(self, coordinator):
    #     """
    #     Check if the task is received by a specific coordinator.
    #     """
    #     return coordinator in self.received_by.all()

    def mark_as_completed(self):
        """
        Marks the task as completed.
        """
        self.completed = True
        self.save()

    def is_completed(self):
        """
        Check if the task is completed.
        """
        return self.completed

    def __str__(self):
        return self.task_name
    class Meta:
        verbose_name = 'Topshiriqlar '
        verbose_name_plural = 'Topshiriqlar umumiy'
        
class TaskCompletion(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,  verbose_name='Topshiriqlar')
    coordinator = models.ForeignKey(Kordinators, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(default=timezone.now, verbose_name='Topshirilgan vaqt')
    title = models.CharField(max_length=100, verbose_name='Sarlahasi')
    description = models.TextField(verbose_name='Tavsifi')
    completed_file = models.FileField(upload_to='completed_tasks/', blank=True, null=True, verbose_name='Biriktirilgan fayl')
    is_late_submission = models.BooleanField(default=False, verbose_name='Topshiriqlar kechikib yuborilgan yo\'q ❌/✅ ha ') 
    completed = models.BooleanField(default=False, verbose_name='Topshiriqlar xolati ❌/✅')  # Add this line 

    # Existing methods

    def __str__(self):
        return f"Vazifa yakunlangan {self.task.task_name} koordinator ismi {self.coordinator.name}"
    
    def save(self, *args, **kwargs):
        # Mark the associated task as received and completed when a TaskCompletion is created
        if not self.completed:
            self.completed = False
            #self.task.mark_as_received(self.coordinator)
        super(TaskCompletion, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Topshiriqlar ijrosi'
        verbose_name_plural = 'Topshiriqlarning ijrosi'
        
class AddWork(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    file = models.FileField(upload_to = 'work/', null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_tasks')
    accepted = models.BooleanField(default=False)
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Shaxsiy qilingan ishlar'
        verbose_name_plural = 'Shaxsiy qilingan ishlar'

class AddTashabbus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tashabbus = models.CharField(max_length=255, verbose_name='Tashabbus nomi')

    def __str__(self):
        return self.tashabbus

    class Meta:
        verbose_name = 'Tashabbus nomi'
        verbose_name_plural = 'Tashabbuslar nomi'

class AddTashabbusCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tashabbus = models.ForeignKey(AddTashabbus, on_delete=models.CASCADE,  verbose_name='Tashabbus nomi')
    tashabbus_category = models.CharField(max_length=255, verbose_name='TAshabbus kategoriyasi')
    def __str__(self):
        return self.tashabbus_category
        
    class Meta:
        verbose_name = 'Tashabbus nomi'
        verbose_name_plural = 'Tashabbus yo\'nalishlari'

class TashabbusTadbir(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tashabbus = models.ForeignKey(AddTashabbus, on_delete=models.CASCADE,  verbose_name='Tashabbus nomi')
    tashabbus_category = models.ForeignKey(AddTashabbusCategory,on_delete=models.CASCADE, verbose_name='TAshabbus kategoriyasi')
    title = models.CharField(max_length=255, verbose_name='Tadbir sarlavhasi')
    content = models.TextField(max_length=255, verbose_name='Tadbir mazmuni')
    file = models.FileField(upload_to='tashabbus/', verbose_name='Faylni briktiring mavjud bo\'lsa', null=True, blank=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Tashabbus tadbir'
        verbose_name_plural = 'Tashabbus tadbirlari'

###### intelektual loyihalar


class AddIntelektual(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    intelektual = models.CharField(max_length=255, choices=intelektual,  verbose_name='Intelektual loyiha nomi')
    title = models.CharField(max_length=255, verbose_name='Tadbir sarlavhasi')
    content = models.TextField(max_length=255, verbose_name='Tadbir mazmuni')
    date = models.DateTimeField(auto_now=False, verbose_name='Vaqti')
    file = models.FileField(upload_to='tashabbus/', verbose_name='Faylni briktiring mavjud bo\'lsa', null=True, blank=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Intelektual'
        verbose_name_plural = 'Intelektual loyiha tadbirlari'

#end intelektual
        
class Qalqon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fakultet = models.CharField(max_length=255, choices=fakultets, verbose_name='Fakultetni tanlang')
    yigit_jamoa_soni = models.IntegerField(verbose_name='Yigit bolalar soni')
    qiz_jamoa_soni = models.IntegerField(verbose_name='Qiz bolalar soni')
    all_stat_file = models.FileField(upload_to='qalqon/', verbose_name='Faylni briktiring mavjud bo\'lsa', null=True, blank=True)
    @classmethod
    def count_boys_girls(cls):
        total_boys = cls.objects.aggregate(Sum('yigit_jamoa_soni'))['yigit_jamoa_soni__sum'] or 0
        total_girls = cls.objects.aggregate(Sum('qiz_jamoa_soni'))['qiz_jamoa_soni__sum'] or 0
        return total_boys, total_girls
    
    class Meta:
        verbose_name = 'Qalqon'
        verbose_name_plural = 'Qalqon jamoasining ro\'yxati'

class Tavsiyanoma(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fakultet = models.CharField(max_length=255, choices=fakultets, verbose_name='Fakultetni tanlang')
    yigit_jamoa_soni = models.IntegerField(verbose_name='Yigit bolalar soni')
    qiz_jamoa_soni = models.IntegerField(verbose_name='Qiz bolalar soni')
    all_stat_file = models.FileField(upload_to='tavsiyanoma/', verbose_name='Faylni briktiring mavjud bo\'lsa', null=True, blank=True)
    @classmethod
    def count_boys_girls(cls):
        total_boys = cls.objects.aggregate(Sum('yigit_jamoa_soni'))['yigit_jamoa_soni__sum'] or 0
        total_girls = cls.objects.aggregate(Sum('qiz_jamoa_soni'))['qiz_jamoa_soni__sum'] or 0
        return total_boys, total_girls
        
    class Meta:
        verbose_name = 'Tavsiya noma'
        verbose_name_plural = 'Tavsiya noma asosida ta\'lim oluvchilar'


class Utizbeshfoiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fakultet = models.CharField(max_length=255, choices=fakultets, verbose_name='Fakultetni tanlang')
    yigit_jamoa_soni = models.IntegerField(verbose_name='Yigit bolalar soni')
    qiz_jamoa_soni = models.IntegerField(verbose_name='Qiz bolalar soni')
    all_stat_file = models.FileField(upload_to='uttizbesh/', verbose_name='Faylni briktiring mavjud bo\'lsa', null=True, blank=True)
    @classmethod
    def count_boys_girls(cls):
        total_boys = cls.objects.aggregate(Sum('yigit_jamoa_soni'))['yigit_jamoa_soni__sum'] or 0
        total_girls = cls.objects.aggregate(Sum('qiz_jamoa_soni'))['qiz_jamoa_soni__sum'] or 0
        return total_boys, total_girls
        
    class Meta:
        verbose_name = '35% lik'
        verbose_name_plural = '35% lik kontrakt asosida ta\'lim oluvchilar'
