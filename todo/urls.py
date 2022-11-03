from django.urls import path

from todo import views

urlpatterns = [
    path('to-do-app/', views.TodoCreateView.as_view(), name='to_do_app'),
    path('delete-task-modal/<int:pk>', views.delete_task_modal, name='delete_modal')


]