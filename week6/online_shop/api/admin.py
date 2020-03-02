from django.contrib import admin

from .models import OnlineProduct, OfflineProduct


admin.site.register(OnlineProduct)


@admin.register(OfflineProduct)
class OfflineProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
