from django.db import models

from customer.models import Customer
from member.models import Member


class Project(models.Model):

    status_options = (('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('on_hold', 'On hold'),
                      ('cancelled', 'Cancelled'), ('finished', 'Finished'))

    project_name = models.CharField(max_length=50)
    status = models.CharField(choices=status_options, max_length=11)
    estimated_hours = models.IntegerField()
    members = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    deadline = models.DateField()
    start_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.project_name} {self.customer}'
