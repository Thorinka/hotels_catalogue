from django.contrib import admin

from cities.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name')
    search_fields = ('city_name',)

