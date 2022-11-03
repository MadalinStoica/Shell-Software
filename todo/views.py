from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from todo.forms import TodoForm
from todo.models import Todo


# Create your views here.

class TodoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'todo/todo_app.html'
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('to_do_app')

    def get_context_data(self, **kwargs):
        data = super(TodoCreateView, self).get_context_data(**kwargs)
        tasks = Todo.objects.all()
        data['all_tasks'] = tasks

        return data




def delete_task_modal(request, pk):
    Todo.objects.filter(id=pk).delete()
    return redirect('to_do_app')