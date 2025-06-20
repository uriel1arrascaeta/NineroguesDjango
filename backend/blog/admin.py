from django.contrib import admin
from . import models

admin.site.register(models.Category)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }
