from django.contrib import admin
from .models import Post, Comments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('staus', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'staus', 'created_on')
    search_fields = ('title', 'content')


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    
    def approve_comments(self, reques, queryset):
        queryset.update(approved=True)