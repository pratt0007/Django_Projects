from django.contrib import admin

# Register your models here.
from .models import image

@admin.register(image)
class imageadmin(admin.ModelAdmin):
    list_display = ['id' , 'photo' , 'date']
    