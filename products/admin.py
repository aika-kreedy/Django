from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "description")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)


