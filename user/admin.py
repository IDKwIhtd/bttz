from django.contrib import admin
from import_export.admin import ExportMixin
from import_export import resources
from .models import Profile, CustomUser


# Register your models here.
class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile


class ProfileAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ProfileResource


class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser


class CustomUserAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CustomUserResource


admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
