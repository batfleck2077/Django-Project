from django import views
from application import views
from django.urls import path

urlpatterns=[

    path('',views.frontpage,name='frontpage'),
    path('index',views.index,name='index'),
    path('forms',views.forms,name='forms'),
]