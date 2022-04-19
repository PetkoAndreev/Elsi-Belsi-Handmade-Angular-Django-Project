from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from elsi_belsi_handmade.elsi_belsi_auth.models import Profile

UserModel = get_user_model()


# TabularInline
class UserProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'
    can_delete = False
    max_num = 1
    verbose_name_plural = 'profile'


# Extended default user admin
@admin.register(UserModel)
class ElsiBelsiHandmadeUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions',
         {
             'fields': (
                 'is_staff',
                 'is_superuser',
                 'groups',
                 'user_permissions',
             ),
         }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email',)

    readonly_fields = ('date_joined',)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, ElsiBelsiHandmadeUserAdmin)
