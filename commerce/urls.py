from django.urls import path
from . import views

urlpatterns = [
    path('', views.commerce_home, name='home'),
    path('contattaci', views.commerce_contattaci, name='contattaci'),
    path('carrello', views.commerce_carrello, name='carrello'),
]
