from django.contrib import admin
from project.models import Signup, register, profile, addProduct
# Register your models here.

admin.site.register(Signup)

@admin.register(register)
class registerAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'username', 'dob', 'gender', 'qualification', 'occupation', 'mobile_no', 'email']

@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    list_display = [ 'companyname','user', 'gender','dob',  'userqualification', 'userdesignation', 'mobileno', 'profile_image', 'companydescription']

@admin.register(addProduct)
class addproductAdmin(admin.ModelAdmin):
    list_display = ['user', 'pname', 'ptype', 'pcategory', 'best_before', 'cost', 'packaging_Details', 'preferred_consumer', 'About_product', 'product_image']