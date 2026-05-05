from django.contrib import admin
from .models import Notice

# MODULE 3: Admin Interface Activation
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
