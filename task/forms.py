from django import forms
from django.forms import TextInput, Select, DateInput, Textarea

from task.models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'project', 'start_date', 'status', 'deadline', 'assignees', 'description']

        widgets = {
            'task_name': TextInput(attrs={'placeholder': 'Please enter task name',
                                          'class': 'form-control'}),
            'project': Select(attrs={'class': 'form-select'}),
            'status': Select(attrs={'class': 'form-select'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'deadline': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'assignees': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description',
                                           'class': 'form-control'})

        }