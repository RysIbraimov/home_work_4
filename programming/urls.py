from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('',views.course_list,name='course_list'),
    path('course_create/',views.course_create,name='course_create'),
]
