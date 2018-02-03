from django.contrib import admin

from .models.user import User


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
