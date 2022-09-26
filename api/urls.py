from .views import task_list,task_detail,add_task,update_task,delete_task
from django.urls import path

urlpatterns = [
    path('list/',task_list,name='tasklist'),
    path('<int:pk>/',task_detail,name='taskdetail'),
    path('add/',add_task,name='addtask'),
    path('update/<int:pk>/',update_task,name='updatetask'),
    path('delete/<int:pk>/',delete_task,name='deletetask'),
]