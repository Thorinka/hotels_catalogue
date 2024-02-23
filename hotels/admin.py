from django.contrib import admin

from hotels.models import Hotel


# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_name', 'address', 'phone_number', 'email', 'city_name')
    search_fields = ('hotel_name', 'email', 'city_name',)
    autocomplete_fields = ['city']

    def city_name(self, obj):
        return obj.city.city_name

    city_name.short_description = 'Город'
