from django.contrib import admin
from .models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', )
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name',)
    list_filter = ('id',)


admin.site.register(UserProfile, UserAdmin)
