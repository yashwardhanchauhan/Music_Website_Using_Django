from django.contrib import admin
from .models import Songs
from django.shortcuts import render
from django.urls import path

#Register your models here.
# class AdminSite(object):
#     pass

# from django.contrib.admin import AdminSite
# from django.http import HttpResponse

# class MyAdminSite(AdminSite):
#     login_template = "admin/login.html"
#     index_template="admin/index.html"
#     def get_urls(self):
        
#         urls = super().get_urls()
#         urls += [
#              path('add_department/', self.admin_view(self.add_department)),
#              path('add_equipment/',self.admin_view(self.add_equipment)),
#              path('add_engineer/',self.admin_view(self.add_engineer))
#         ]
#         return urls

#     def add_department(self, request):
#         return render(request,"admin/add_department.html")


#     def add_equipment(self,request):
#         return render(request,"admin/add_equipment.html")
    
#     def add_engineer(self,request):
#         return render(request,"admin/add_engineer.html")

# admin_site = MyAdminSite()
    
admin.site.register(Songs)