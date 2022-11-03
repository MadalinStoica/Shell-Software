from django.urls import path

from task import views

urlpatterns = [

    path('new_task_project/<int:pk>', views.NewTaskIntoProjectCreateView.as_view(), name='new-task-project'),
    path('update_task_project/<int:pk>', views.TaskUpdateIntoProjectView.as_view(), name='update-task-project'),
    path('delete_task_modal/<int:pk>', views.delete_task_modal, name='delete-task-modal'),

]