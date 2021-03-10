from accounts.models import CustomUser
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(
        verbose_name='カテゴリー名',
        max_length=127,

    )
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(
        verbose_name='企業名',
        max_length=127,
    )

    deadline = models.DateTimeField(
        verbose_name='提出期限',
        default=timezone.now
    )

    def __str__(self):
        return self.name

    def deadline_mdHM(self):
        return self.deadline.strftime('%月%d日%H:%M')

class EntrySheet(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.PROTECT,
    )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='本文',
        blank=True,
        null=True,
    )
    content_max_length = models.SmallIntegerField(
        verbose_name='最大文字数',
        blank=True,
        null=True,
    )
    content_min_length = models.SmallIntegerField(
        verbose_name='最小文字数',
        blank=True,
        null=True,
    )
    photo1 = models.ImageField(
        verbose_name='写真1',
        blank=True,
        null=True,
    )
    photo2 = models.ImageField(
        verbose_name='写真2',
        blank=True,
        null=True,
    )
    photo3 = models.ImageField(
        verbose_name='写真3',
        blank=True,
        null=True,
    )
    is_public = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name='作成日時',
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True,
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name='カテゴリー',
        blank=True,
    )
    companies = models.ManyToManyField(
        Company,
        verbose_name='企業',
        blank=True,
    )


    def __str__(self):
        return self.title
