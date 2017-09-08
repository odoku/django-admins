# -*- coding: utf-8 -*-

from django.contrib.admin import ModelAdmin, register, StackedInline

from .models import Article, Category, Comment, Tag


class CommentInline(StackedInline):
    model = Comment
    extra = 0
    min_num = 0


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)


@register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'modified_at')
    list_filter = ('category',)
    search_fields = ('title', 'user__username')
    inlines = [CommentInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ArticleAdmin, self).save_model(request, obj, form, change)


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name',)
