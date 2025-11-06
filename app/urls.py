from django.urls import path

from .views import home_view,create_task,task_list

app_name = 'tasks'

urlpatterns = [
        path('',home_view,name='home_page'),
        path('add/',create_task,name='create_page'),
        path('task/',task_list,name='task_page'),
]
