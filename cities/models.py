from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=30, verbose_name='название')

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.city_name
