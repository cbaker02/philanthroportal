from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

from .models import Nfp, Corporation, Grant, GrantApplication

admin.site.register(Nfp)
admin.site.register(Corporation)
admin.site.register(Grant)
admin.site.register(GrantApplication)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email"]
    ordering = ["email"]

    list_display = ('email',)
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone', 'profile_image', 'account_type')})
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email','password1', 'password2', 'name', 'phone', 'profile_image'),
    }),
)

admin.site.register(CustomUser, CustomUserAdmin)
