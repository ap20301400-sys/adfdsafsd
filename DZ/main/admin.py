from django.contrib import admin
from .models import Notice

# Register your models here.
class AdminNotice(admin.ModelAdmin):
    list_display = ('title','author_name', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)  

    

admin.site.register(Notice , AdminNotice)