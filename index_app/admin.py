from django.contrib import admin
# from index_app.models import SystemInfo, UserInfo
from index_app.models import SystemInfo
from django.contrib.auth.models import Group, User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username',)

class SystemInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'mark')
    search_fields = ('name', 'type',)
    list_filter = ('name',)

# admin.site.register(UserInfo, UserAdmin)
admin.site.register(SystemInfo, SystemInfoAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
