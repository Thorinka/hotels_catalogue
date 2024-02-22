from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from cities.models import City


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=60, verbose_name='название отеля')
    address = models.CharField(max_length=150, verbose_name='адрес')
    phone_number = PhoneNumberField(verbose_name='номер телефона')
    email = models.EmailField(verbose_name='электронная почта')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='город')

    class Meta:
        verbose_name = 'отель'
        verbose_name_plural = 'отели'
