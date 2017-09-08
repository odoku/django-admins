# -*- coding: utf-8 -*-

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=20)

    class Meta:
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=20)

    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'

    def __str__(self):
        return self.name


def article_mainvisual_upload_to(instance, filename):
    return filename


class Article(models.Model):
    user = models.ForeignKey(
        'accounts.User',
        verbose_name='ユーザー',
        related_name='articles',
        editable=False,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        related_name='articles',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='タグ',
        related_name='articles',
    )

    main_visual = models.ImageField(
        'メインビジュアル',
        upload_to=article_mainvisual_upload_to,
    )
    title = models.CharField('タイトル', max_length=50)
    body = RichTextUploadingField('内容')

    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    modified_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        verbose_name='記事',
        related_name='comments',
    )
    body = models.TextField('内容')

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'
