from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
  search_fields = ['full_name', 'username', 'phone_number', 'email']
  list_display = ['full_name', 'username', 'email', 'phone_number']
  
admin.site.register(User, UserAdmin)
    

