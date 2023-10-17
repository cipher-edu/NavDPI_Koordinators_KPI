from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('task/<int:task_id>/assign/', TaskAssignmentView.as_view(), name='task_assignment'),
    path('task/<int:task_id>/confirm/', TaskConfirmationView.as_view(), name='task_confirmation'),
    path('task/<int:task_id>/reject/', TaskRejectionView.as_view(), name='task_rejection'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)