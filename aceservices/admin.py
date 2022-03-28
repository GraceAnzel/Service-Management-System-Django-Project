from django.contrib import admin


from .models import Product, Service
from .models import Category
from .models import User,add,Product,payuser



class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminService(admin.ModelAdmin):
    list_display = ['name','description']




# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(User)
admin.site.register(add)
admin.site.register(Service,AdminService)
admin.site.register(payuser)