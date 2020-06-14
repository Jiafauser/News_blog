from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.course_list, name='course_list'),

]
