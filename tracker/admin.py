from django.contrib import admin
from .models import BloodPressureRecord

@admin.register(BloodPressureRecord)
class BloodPressureRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'systolic', 'diastolic', 'date')
    list_filter = ('user', 'date')
    search_fields = ('user__username', 'systolic', 'diastolic')
    date_hierarchy = 'date'