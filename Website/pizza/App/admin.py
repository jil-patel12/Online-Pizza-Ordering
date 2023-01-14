
from django.contrib import admin

# Register your models here.
from .models import user_extra
from .models import menu1
class user_extra_admin(admin.ModelAdmin):
    list_display = ('full_name','phone_no','user_address1','user_address2','city','state','Date_of_birth',)
    list_per_page = 5
    search_fields = ('full_name',)
    list_filter = ('full_name',)

class menu_admin(admin.ModelAdmin):
    list_display = ('id', 'name',  'price', )
    list_per_page = 5


admin.site.register(user_extra,user_extra_admin)
admin.site.register(menu1,menu_admin)

