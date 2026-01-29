from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from app.models import trust_profile, Donation, Utilization


# Inline Trust Profile inside User admin
class trust_profile_Inline(admin.StackedInline):
    model = trust_profile
    can_delete = False
    verbose_name_plural = 'Trust Profile'


class CustomaizedUserAdmin(UserAdmin):
    inlines = (trust_profile_Inline,)


# Re-register User with Trust Profile inline
admin.site.unregister(User)
admin.site.register(User, CustomaizedUserAdmin)


# Register models
admin.site.register(trust_profile)
admin.site.register(Donation)
admin.site.register(Utilization)
