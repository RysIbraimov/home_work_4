from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import TeacherForm

class TeacherList(generic.ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'teacher_list.html'

class CreateTeacher(generic.CreateView):
    model = Teacher
    fields = '__all__'
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')

