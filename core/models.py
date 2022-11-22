from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# class Admin(models.Model):
#     id_account = models.AutoField(primary_key=True)
#     account = models.ForeignKey(User, on_delete=models.CASCADE)
#     account_type = models.TextField(blank=True)
#     password = pass
#     fk_id_staff = pass
#
#     # profileimg = models.ImageField(
#     #     upload_to='profile_images', default='blank-profile-picture.png')
#     # location = models.CharField(max_length=100, blank=True)
#     def __str__(self):
#         return self.account.username

class Staff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    name_staff = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    birthday_staff = models.DateField()
    sex_staff = models.CharField(max_length=10, blank=True)
    address_staff = models.CharField(max_length=255, blank=True)
    phone_staff = models.IntegerField()

    def __str__(self):
        return self.name_staff.username




