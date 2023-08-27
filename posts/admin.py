from django.contrib import admin
from posts.models import Post, Commets

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status"]
    list_filter = ["status", ]
    list_editable = ["status",]

@admin.register(Commets)
class CommetAdmin(admin.ModelAdmin):
    list_display = ["post", "name", "created"]