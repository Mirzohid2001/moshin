from django.contrib import admin
from .models import Partner, Partnership

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'is_active', 'order', 'created_at']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description', 'email']
    ordering = ['order']

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ['partner', 'partnership_type', 'start_date', 'end_date', 'is_active']
    list_editable = ['is_active']
    list_filter = ['partnership_type', 'is_active', 'start_date']
    search_fields = ['partner__name', 'description']
    date_hierarchy = 'start_date'
