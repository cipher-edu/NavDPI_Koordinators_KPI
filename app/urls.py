from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('', home, name='home'),
    # path('register/', user_login, name='login')
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complate'),
    path('signup/', SingUpView.as_view(), name='signup'),
    path('profile/', dashboard, name='dashboard'),
    path('kordinators/', kordinators_list, name='kordinators_list'),
    path('user/profile/', user_profile, name='user_profile'),
    path('update_kordinator_profile/', update_kordinator_profile, name='update_kordinator_profile'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/assign/<uuid:task_id>/', assign_task, name='assign_task'),
    #path('tasks/mark-received/<uuid:task_id>/',mark_task_received, name='mark_task_received'), #vazifani qabul qilib olganligi haqida url
    #path('task/<uuid:task_id>/', task_detail, name='task_detail'),
    path('tasks/complete/<uuid:task_id>/', task_completion, name='task_completion'),
    path('send-task/', send_task, name='send_task'),
    path('add-task/', create_task, name='add_task'),
    path('statistics/', stats, name='stats'),
    path('complations/', task_completion_status, name='complation'),
    path('qalqon/', save_qalqon_info, name='qalqon'),
    # path('qalqon/', QalqonModalView.as_view(), name='qalqon_modal'),
    path('qalqon/<int:pk>/edit/', QalqonUpdateView.as_view(), name='qalqon_edit'),
    path('qalqon/4364c33-f553-4ea4cliaent?TabLinkquery/<int:pk>/?&&926f-d0bf8668f914&delete?cliaent?/query/', QalqonDeleteView.as_view(), name='qalqon_delete'),

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

