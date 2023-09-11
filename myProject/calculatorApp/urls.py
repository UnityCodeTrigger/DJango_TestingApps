from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submitquery',views.submitquery,name='submitquery')    #El form hace referencia a este url el cual esta referenciando a views.submitquery para enviarle informacion
]
