from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('add_user/', views.add_user, name='add_user'),
    path('logout/', views.logout_user, name='logout'),
    path('register_pass/', views.register_pass, name='register_pass'),

       # Change Password
    path('change_password/', views.change_password, name='change_password'),
    path('password_change_done/', views.password_change_done, name='password_change_done'),
    # Reset Password
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password-reset/password_reset_form.html',
        email_template_name='password-reset/password_reset_email.html',
        subject_template_name='password-reset/password_reset_subject.txt',
        success_url='/password_reset_done/'
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password-reset/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password-reset/password_reset_confirm.html',
        success_url='/password_reset_complete/'
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password-reset/password_reset_complete.html'
    ), name='password_reset_complete'),
]

