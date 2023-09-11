from django.db import models

# Create your models here.

class Records(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
