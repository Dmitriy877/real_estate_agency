from django.contrib import admin

from .models import Flat, Complain, Owner


class OwnerInstanceInline(admin.StackedInline):
    model = Owner.flat_property.through
    raw_id_fields = ["owner"]


class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerInstanceInline]
    search_fields = ["town", "town_district", "address"]
    readonly_fields = ["created_at"]
    list_display = (
        "address",
        "price",
        "new_building",
        "construction_year",
        "town"
    )
    list_editable = ["new_building"]
    list_filter = ("new_building", "rooms_number", "has_balcony")
    raw_id_fields = ["who_liked"]


class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat"]


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat_property"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
