from collections import Counter
from itertools import count
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html,urlencode
from django.urls import reverse



# Register your models here.
from . import models
@admin.register(models.Product)    ## register modles in admin site  and show unit price
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','inventory_status','collection']
    list_editable = ['unit_price']
    @admin.display(ordering='inventory')   # Sort the list by inventory 
    def inventory_status(self,product):    # let inventory < 10 show "Low " other show "Good "
        if product.inventory < 10:
            return "Low"
        else:
            return "Good"
   

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):                                           # Find one customers's all information of id
    list_display = ['first_name','last_name','membership','order_amount']
    list_editable=['membership']
    @admin.display(ordering='order_amount')                                     # order customer by order_amount

    def order_amount(self,customer):                                            # apply http://127.0.0.1:8000/admin/store/order/?customer__id=11   search all order with id = 11
        url = (
            reverse('admin:store_order_changelist')
            +'?'
            +urlencode({
                'customer__id':str(customer.id)
            })
        )
        return format_html('<a href="{}">{}</a>',url,customer.order_amount)             #  use this format to link to other page
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_amount = Count('order')
        )
    
    

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','order_detail']
    list_select_related = ['customer']                  # preorder same use as "selected realted" in query
    def order_detail(self,order):
            return order.customer


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']

    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url =( 
            reverse('admin:store_product_changelist')             # filter format is http://127.0.0.1:8000/admin/store/product/?collection__id=1   apply all collection =1 prodcut
            +'?' 
            +urlencode({
                'collection__id': str(collection.id)                       
            }

            ) )           # admin : app_models_page     use this format
        return format_html('<a href="{}">{}</a>',url,collection.products_count)
    
    def get_queryset(self, request):                            # Show the number of product in collectons by override query set
        return super().get_queryset(request).annotate(  
            products_count = Count('product')
            )

# admin.site.register(models.Customer)
# admin.site.register(models.Product,ProductAdmin)