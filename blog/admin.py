from django.contrib import admin
from .models import CompanyInfo, CompanyCapability, BlogPost

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(CompanyCapability)
class CompanyCapabilityAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    ordering = ['order']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published', 'created_at']
    list_editable = ['published']
    search_fields = ['title', 'content']
    list_filter = ['published', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
