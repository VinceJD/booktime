from django import views
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Home, name='home'),
    path('about_us/', views.About_us, name='about_us'),
    #path('contact_us/', views.Contact_us_view.as_view(), name='contact_us')
]