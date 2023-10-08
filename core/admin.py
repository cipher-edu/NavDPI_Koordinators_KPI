from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.
class KordinatorAdmin(admin.ModelAdmin):
    list_display=('name','lastname','surname','age', 'fak','ilimiy_darajasi','kor_lavozimi','tel','get_html_photo',)
    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')
        return None
    get_html_photo.short_description = 'Surati'
    list_filter=('kor_lavozimi',)


admin.site.register(Kordinators, KordinatorAdmin)