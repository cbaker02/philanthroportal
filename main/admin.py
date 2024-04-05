from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

from .models import Nfp, Corporation

admin.site.register(Nfp)
admin.site.register(Corporation)


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
        ('Personal info', {'fields': ('name', 'phone')})
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email','password1', 'password2', 'name', 'phone', 'profile_image'),
    }),
)

admin.site.register(CustomUser, CustomUserAdmin)

