from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from task.forms import NewTaskForm
from task.models import Task


# Create your views here.

class NewTaskIntoProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task/new_task.html'
    model = Task
    form_class = NewTaskForm
    # success_url = '/details_project/{project_id}' # sau o alta varianta

    def get_success_url(self):
        return reverse('details_project', kwargs={'pk': self.object.project_id})


class TaskUpdateIntoProjectView(UpdateView):
    template_name = 'task/update_task_into_project.html'
    model = Task
    form_class = NewTaskForm
    success_url = '/details_project/{project_id}'


# de gasit solutie spre directionare project/project_id
def delete_task_modal(request, pk):
    task_to_be_deleted = Task.objects.filter(id=pk).get()
    project_id = task_to_be_deleted.project_id
    task_to_be_deleted.delete()
    return redirect(reverse('details_project', kwargs={'pk': project_id}))



