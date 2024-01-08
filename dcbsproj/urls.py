from django.urls import path
from users import views as user_views
from . import views

app_name = 'dcbsproj'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]