# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(
            username=username,
            last_login=timezone.now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, **extra_fields):
        return self._create_user(username=username, **extra_fields)

    def create_superuser(self, username, **extra_fields):
        return self._create_user(
            username=username,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    username = models.CharField('ユーザー名', max_length=50, unique=True)
    is_superuser = models.BooleanField('管理者', default=False)
    is_staff = models.BooleanField('スタッフ', default=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    modified_at = models.DateTimeField('更新日時', auto_now=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_group_permissions(self, obj=None):
        return set()

    def get_all_permissions(self, obj=None):
        return set()

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username
