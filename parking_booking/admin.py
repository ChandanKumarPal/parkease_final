# from django.contrib import admin
# from .models import Slot , Booking
# # Register your models here.

# admin.site.register(Slot)
# admin.site.register(Booking)



# new code and logic start from  here 


from django.contrib import admin
from .models import Booking, Slot
from django.http import HttpResponse
import csv

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'slot', 'start_time', 'end_time', 'vehicle_number', 'price')  # Fields to display in the admin list view
    list_filter = ('slot', 'start_time', 'end_time')  # Fields to filter by in the admin interface
    search_fields = ('user__username', 'vehicle_number')  # Fields to search by in the admin interface

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=bookings.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected Bookings as CSV"

admin.site.register(Booking, BookingAdmin)
admin.site.register(Slot)
