from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "property_type", "status", "price", "featured", "updated_at")
    list_filter = ("status", "property_type", "featured", "location")
    search_fields = ("title", "location", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-updated_at",)
    inlines = [PropertyImageInline]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ("property", "image")
    search_fields = ("property__title", "property__location")
