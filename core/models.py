from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Staff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    name_staff = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    birthday_staff = models.DateField()
    sex_staff = models.CharField(max_length=10, blank=True)
    address_staff = models.CharField(max_length=255, blank=True)
    phone_staff = models.IntegerField()

    def __str__(self):
        return self.name_staff.username
