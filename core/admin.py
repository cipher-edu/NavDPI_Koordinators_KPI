from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.forms.widgets import CheckboxSelectMultiple
from .models import *

class ImageCheckboxSelectMultiple(CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        images_html = ''.join([
            f'<img src="{image.image.url}" style="height: 100px; margin-right: 5px;" />'
            for image in self.choices.queryset
        ])
        return format_html('{}<div>{}</div>', output, mark_safe(images_html))

class KordinatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'surname', 'age', 'fak', 'ilimiy_darajasi', 'kor_lavozimi', 'tel', 'get_html_photo',)
    list_filter = ('kor_lavozimi',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')
        return None

    get_html_photo.short_description = 'Surati'

# Register Kordinators with KordinatorAdmin
admin.site.register(Kordinators, KordinatorAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'image']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="100">')
        return None

    image_preview.short_description = 'Image Preview'

admin.site.register(Image, ImageAdmin)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_content', 'author', 'date_posted', 'category', 'display_selected_images']
    formfield_overrides = {
        models.ManyToManyField: {'widget': ImageCheckboxSelectMultiple},
    }

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.images.set(Image.objects.all())

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'images':
            kwargs['queryset'] = Image.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def display_selected_images(self, obj):
        images = obj.images.all()
        if images:
            return mark_safe(''.join(f'<img src="{image.image.url}" style="height: 100px; margin-right: 5px;" />' for image in images))
        return None

    display_selected_images.short_description = 'Selected Images'

admin.site.register(Posts, PostsAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','content', 'given_time', 'submission_time', 'assigned_to', 'is_delayed',)

admin.site.register(Task, TaskAdmin)