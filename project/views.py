from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from project.forms import NewProjectForm
from project.models import Project
from task.models import Task


class NewProjectCreateView(CreateView):
    template_name = 'project/new_project.html'
    model = Project
    form_class = NewProjectForm
    success_url = reverse_lazy('projects')


class ProjectsListView(ListView):
    template_name = 'project/projects.html'
    model = Project
    context_object_name = 'all_projects'


class ProjectUpdateView(UpdateView):
    template_name = 'project/update_project.html'
    model = Project
    form_class = NewProjectForm
    success_url = reverse_lazy('projects')


def delete_project_modal(request, pk):
    Project.objects.filter(id=pk).delete()
    return redirect('projects')


class ProjectDetailView(DetailView):
    template_name = 'project/details_project.html'
    model = Project

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        tasks = Task.objects.all().filter(project_id=data['project'].id)
        data['all_tasks'] = tasks
        print(data)
        return data
