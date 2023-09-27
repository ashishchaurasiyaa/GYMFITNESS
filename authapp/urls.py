from django.urls import path
from authapp import views

urlpatterns = [
    path('home/',views.Home, name='Home')
]
