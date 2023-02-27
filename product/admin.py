from django.contrib import admin

from .models import Product, Variation


class VariationInline(admin.TabularInline):
    model = Variation 
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_formatted_price', 'get_formatted_price_promotional']
    inlines = [
        VariationInline
    ]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)