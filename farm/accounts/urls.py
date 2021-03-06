from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)



urlpatterns = [
    #url(r'^$', views.home, name='account'),
    path('', views.homeAccount, name='account'),
    #I've deleted also old homeAccount.html
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('register/', views.register, name='register' ),
    path('profile/', views.view_profile, name='view_profile'),
    #path('profile/(?P<pk>\d+)/', views.view_profile, name='view_profile_with_pk'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('change-password', views.change_password, name='change_password'),

    path('reset-password', password_reset,{'template_name': 'accounts/reset_password.html', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),


    path('reset-password/done', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),


    path('reset-password/confirm/<uidb64>/<token>/', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html'}, name='password_reset_confirm'),

    path('reset-password/complete', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete' )
]