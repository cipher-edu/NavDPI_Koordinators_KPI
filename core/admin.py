from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.forms import ImageField
from django.db import models

class KordinatorAdmin(admin.ModelAdmin):
    list_display=('name','lastname','surname','age', 'fak','ilimiy_darajasi','kor_lavozimi','tel','get_html_photo',)
    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')
        return None
    get_html_photo.short_description = 'Surati'
    list_filter=('kor_lavozimi',)


admin.site.register(Kordinators, KordinatorAdmin)

# class AdminPost(admin.ModelAdmin):
#     list_display = ['post_title', 'post_content', 'author', 'date_posted', 'category']
#     inlines = [ImageInline]
#     def get_html_photo(self, obj):
#         if obj.image:
#             return mark_safe(f'<img src="{obj.image.url}" width="50">')
#         return None
#     get_html_photo.short_description = 'Surati'
# admin.site.register( Posts, AdminPost)

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['image_preview', 'image']

#     def image_preview(self, obj):
#         if obj.image:
#             return mark_safe(f'<img src="{obj.image.url}" height="100">')
#         return None

#     image_preview.short_description = 'Image Preview'
#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         # Custom logic to display images associated with the Posts object
#         posts = Posts.objects.filter(image_id=object_id)
#         images = posts.first().photos.all() if posts.exists() else []
#         extra_context = {'images': images}
#         return super().change_view(request, object_id, form_url, extra_context)

#     image_preview.short_description = 'Image Preview'

# admin.site.register(Image, ImageAdmin)
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

    def display_selected_images(self, obj):
        images = obj.images.all()
        if images:
            return mark_safe(''.join(f'<img src="{image.image.url}" style="height: 100px; margin-right: 5px;" />' for image in images))
        return None

    display_selected_images.short_description = 'Selected Images'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'images':
            # Modify the queryset for the images field to show images as thumbnails
            kwargs['queryset'] = Image.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Posts, PostsAdmin)