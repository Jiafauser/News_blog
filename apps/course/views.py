from django.shortcuts import render
from django.views import View


# Create your views here.

def course_list(request):
    return render(request, 'course/course.html')
