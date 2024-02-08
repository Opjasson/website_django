from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('shoes/',views.shoes),
    path('hat/',views.hat)
]
