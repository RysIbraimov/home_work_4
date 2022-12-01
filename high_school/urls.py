from django.urls import path
from  . import views

urlpatterns = [
    path('teacher_list/',views.TeacherList.as_view(),name='teacher_list'),
    path('teacher_create/',views.CreateTeacher.as_view(),name='teacher_create'),

]
