from django.contrib import admin

# Register your models here.

from .models import article

class articleadmin(admin.ModelAdmin):
    list_display=['id','title']#how should we display in admin page[initially its just obj1. obj2 etc.. now we changed it into id and title]
    search_fields=['title','content'] #to create a serach bar in admin/article page 

admin.site.register(article,articleadmin)
