from django.contrib import admin
from products.models import *

admin.site.register(Category)


class ProductImageAdmin(admin.StackedInline):
    model= Product_Image

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_name' , 'price']
    inlines =[ProductImageAdmin]



@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name' , 'price']
    model = ColorVariant



@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name' , 'price']
    model = SizeVariant


admin.site.register(Product, ProductAdmin)


admin.site.register(Product_Image)
#admin.site.register(Category)



# Register your models here.
