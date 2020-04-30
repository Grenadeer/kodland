from django.db import models


class Post(models.Model):
    create_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.create_date.strftime('%d.%m.%Y %H:%M:%S') + " - " + self.title
