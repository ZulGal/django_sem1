from django.contrib import admin
from .models import Coin, Author, Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'birthday']
    ordering = ['name', '-birthday']
    list_filter = ['name', 'birthday']
    search_fields = ['name']
    search_help_text = 'Поиск по полю имя автора'

    readonly_fields = ['birthday']

    fieldsets = [
        (
            'Автор',
            {
                'classes': ['wide'],
                'fields': ['name', 'last_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['birthday', 'bio'],
            },
        ),

        (
            'Прочее',
            {
                'description': 'Контактная информация',
                'fields': ['email'],
            }
        ),
    ]

@admin.action(description="Стереть содержимое поста")
def reset_content(modeladmin, request, queryset):
    queryset.update(content='')
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author']
    ordering = ['title','author']
    list_filter = ['title', 'author']
    search_fields = ['title']
    search_help_text = 'Поиск по полю заголовок'
    actions = [reset_content]

    readonly_fields = ['is_published']

    fieldsets = [
        (
            'Post',
            {
                'classes': ['wide'],
                'fields': ['title', 'content'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Автор ',
                'fields': ['author'],
            },
        ),

        (
            'Other',
            {
                'description': 'Прочая информация',
                'fields': ['is_published', 'views'],
            }
        ),
    ]
admin.site.register(Coin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
