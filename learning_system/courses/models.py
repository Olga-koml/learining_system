from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=settings.MAX_LENGTH_NAME
        )
    owner = models.ForeignKey(
        User,
        verbose_name='собственник продукта',
        on_delete=models.CASCADE,
        related_name='products'
        )
    user = models.ManyToManyField(
        User, verbose_name='студент',
        related_name='student_products',
        blank=True
        )

    class Meta:
        ordering = ['title']
        verbose_name = 'Учебный продукт'
        verbose_name_plural = 'Учебные продукты'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    name = models.CharField(
        verbose_name='Название урока',
        max_length=settings.MAX_LENGTH_NAME
        )
    video_link = models.URLField(verbose_name='Ссылка на видео')
    duration_sec = models.DurationField(
        verbose_name='Длительность просмотра в сек'
        )
    products = models.ManyToManyField(Product, related_name='lessons')

    class Meta:
        ordering = ['-name']
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


class LessonView(models.Model):
    class Status(models.TextChoices):
        VIEWED = 'V', 'Просмотрено'
        NOT_VIEWED = 'NV', 'Не просмотрено'

    user = models.ForeignKey(
        User, verbose_name='Студент',
        on_delete=models.CASCADE
        )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=Status.choices,
        default=Status.NOT_VIEWED
        )
    viewing_time_seconds = models.IntegerField(default=0)
    last_viewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Просмотр урока'
        verbose_name_plural = 'Просмотры уроков'
