from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=70)
    cui = models.IntegerField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
