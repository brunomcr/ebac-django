from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    #prepopulated_fields = {"slug": ("title", )}


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "created_on")
    list_filter = ("active",)
    search_fields = ["author", "content"]
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)
