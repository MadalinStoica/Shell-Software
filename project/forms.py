from django import forms
from django.forms import TextInput, Select, DateInput, Textarea

from project.models import Project


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'customer', 'status', 'estimated_hours', 'members',
                  'deadline', 'description']

        widgets = {
            'project_name': TextInput(attrs={'placeholder': 'Please enter project name',
                                             'class': 'form-control'}),

            'customer': Select(attrs={'class': 'form-select'}),

            'status': Select(attrs={'class': 'form-select'}),

            'estimated_hours': TextInput(attrs={'class': 'form-control'}),

            'members': Select(attrs={'class': 'form-select'}),

            'deadline': DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': Textarea(attrs={'placeholder': 'Please enter your description',
                                             'class': 'form-control'}),

        }