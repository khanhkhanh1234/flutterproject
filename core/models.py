from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

# Create your models here.


class Admin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    id_admin = models.IntegerField()
    bio = models.TextField(blank=True)
    adminimg = models.ImageField(
        upload_to='admin_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    name_customer = models.CharField(max_length=100)
    sex_customer = models.TextChoices('Male', 'Female')
    phone_customer = PhoneNumberField(blank=True)
    citizen_identification = PhoneNumberField(blank=True)
    address_customer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name_customer


class Car_Customer(models.Model):
    id_car = models.AutoField(primary_key=True)
    id_customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
    )
    car_company = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    bien_so = models.CharField(max_length=25, blank=True)

    def __itnit__(self):
        return self.id_customer


class guixe(models.Model):
    id_guixe = models.AutoField(primary_key=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    id_car = models.OneToOneField(
        Car_Customer,
        on_delete=models.CASCADE,
    )
    id_parking = models.OneToOneField(
        'choDoXe',
        on_delete=models.CASCADE,
    )
    id_giave = models.OneToOneField(
        # 'id_giave.Cost',
        'Cost',
        on_delete=models.CASCADE,
    )
    name_customer = models.OneToOneField(
        'Customer',
        on_delete=models.CASCADE,
    )
    tong_tien = models.IntegerField()
    id_bill = models.OneToOneField(
        # 'id_bill.Bill',
        'Bill',
        on_delete=models.CASCADE)
    trang_thai = models.BooleanField()

    def __itnit__(self):
        return self.id_guixe


class choDoXe(models.Model):
    id_parking = models.AutoField(primary_key=True)
    parking_space = models.CharField(max_length=100)
    trang_thai = models.BooleanField()

    def __str__(self):
        return self.parking_space


class Bill(models.Model):
    id_bill = models.AutoField(primary_key=True)
    id_customer = models.OneToOneField(
        Car_Customer,
        on_delete=models.CASCADE,
    )
    trang_thai = models.BooleanField()

    def __itnit__(self):
        return self.id_bill


class Cost(models.Model):
    id_giave = models.AutoField(primary_key=True)
    time = models.TimeField()
    gia_ve = models.IntegerField()

    def __itnit__(self):
        return self.gia_ve


class CheckBienSo(models.Model):
    id_car = models.AutoField(primary_key=True)
    bien_so = models.CharField(max_length=25, blank=True)
    trang_thai = models.BooleanField()
    id_checkbienso = models.ForeignKey(Car_Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.bien_so
