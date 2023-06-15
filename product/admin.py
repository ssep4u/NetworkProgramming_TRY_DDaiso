from django.contrib import admin

from product.models import Product, Review


class ReviewInLine(admin.StackedInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
