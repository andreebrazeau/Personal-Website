from blog.models import BlogPost, Comment
from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created"]

class BlogPostAdmin(admin.ModelAdmin):
    def preview(self, obj):
        return obj.body[0:100]
    list_display = ["title", "author", "preview"]
    search_field = ["title"]

admin.site.register(Comment, CommentAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
