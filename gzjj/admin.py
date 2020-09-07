from django.contrib import admin
from .models import *


from django.utils.text import capfirst
class Gzjjlist(admin.ModelAdmin):
    list_display = ['name','text','stat','cl_name','ctime','utime']
    search_fields = ['name','text']  # display 展示表字段，filter过滤分类，search搜索内容

admin.site.register(Gzjj,Gzjjlist) #工作交接
