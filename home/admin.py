from django.contrib import admin
from .models import Product_Table, Product_Category, color, size, Embroidery, CartItem, Cart
# Register your models here.

admin.site.register(Product_Category)




class product_table_inline_color(admin.TabularInline):
    model = color

class product_table_inline_size(admin.TabularInline):
    model = size

class product_table_inline_Embroidery(admin.TabularInline):
    model = Embroidery


class show_product_Admin(admin.ModelAdmin):
    inlines = [product_table_inline_color, product_table_inline_size, product_table_inline_Embroidery]
    search_fields = ('Product_Name', 'Product_Category', 'availability')
    list_display = ['Product_Name', 'Product_Category', 'availability']
admin.site.register(Product_Table, show_product_Admin)


class Cart_inline_CartItems(admin.TabularInline):
    model = CartItem

class show_Cart(admin.ModelAdmin):
    inlines = [Cart_inline_CartItems]
    search_fields = ['Anonymous_User_session_id']
    list_display = ['Anonymous_User_session_id', 'Total_Cart_Amount']
    readonly_fields = ['Anonymous_User_session_id']
admin.site.register(Cart, show_Cart)