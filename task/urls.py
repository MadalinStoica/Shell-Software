from django.urls import path

from task import views

urlpatterns = [

    path('new_task_project/<int:pk>', views.NewTaskIntoProjectCreateView.as_view(), name='new-task-project')
]