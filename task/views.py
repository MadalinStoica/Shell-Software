from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

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

