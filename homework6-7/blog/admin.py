from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # вывод колонок в админке
    search_fields = ('title', 'content')                 # поиск по этим полям
    list_filter = ('created_at',)                         # фильтр по дате создания
