from django.db import models
from django.utils import timezone


class Post(models.Model):
    create_date = models.DateTimeField(
        default=timezone.now,
        help_text="Дата публикации",
        verbose_name="Опубликован",
    )
    title = models.CharField(
        max_length=200,
        help_text="Заголовок публикации",
        verbose_name="Заголовок",
    )
    text = models.TextField(
        help_text="Текст публикации",
        verbose_name="Текст",
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='post_images',
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.create_date.strftime('%d.%m.%Y %H:%M:%S') + " - " + self.title
