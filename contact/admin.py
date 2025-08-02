from django.contrib import admin
from .models import ContactMessage, ContactInfo

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email']
    fieldsets = (
        ('Контактная информация', {
            'fields': ('address', 'phone', 'email', 'working_hours')
        }),
        ('Карта', {
            'fields': ('map_embed',),
            'description': 'Вставьте HTML код карты (например, Google Maps)'
        }),
    )
