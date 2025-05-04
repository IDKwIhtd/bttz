from django.contrib import admin
from import_export.admin import ExportMixin
from import_export import resources
from .models import Post, Comment


# Register your models here.
class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class PostAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = PostResource


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


class CommentAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CommentResource


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
