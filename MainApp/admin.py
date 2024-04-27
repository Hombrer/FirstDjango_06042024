from django.contrib import admin
from MainApp.models import Color, Item

# Register your models here.
# admin.site.register((Color, Item))


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "count", "display_colors")
    list_filter = ("name", "count")

admin.site.register(Item, ItemAdmin)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_filter = ("name",)