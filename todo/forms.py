from django import forms
from django.forms import TextInput

from todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']

        widgets = {
            'task': TextInput(attrs={'placeholder': 'Write your task..',
                                     'class': 'form-control'}),
        }
        labels = {'task': ''}
