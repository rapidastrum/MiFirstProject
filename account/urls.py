from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [

     # previous login view

     path('', views.index, name='index'),
     path('account/login/', views.user_login, name='login'),
     path('account/logout/', views.user_logout, name='logout'),

     # login / logout urls
     # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
     # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
     # url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
     # url(r'^$', views.dashboard, name='dashboard'),
]