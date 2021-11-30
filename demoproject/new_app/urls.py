from django.contrib import admin
from django.urls import path,include
from . import views

from demoproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]
