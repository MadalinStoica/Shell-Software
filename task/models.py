from django.db import models

from member.models import Member
from project.models import Project


# Create your models here.

class Task(models.Model):

    task_name = models.CharField(max_length=70)
    start_date = models.DateField()
    deadline = models.DateField()

    assignees = models.ForeignKey(Member, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.task_name}'
