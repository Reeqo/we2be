import hashlib
from django.db import models
import datetime


class Video(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Обложка')
    video = models.FileField(upload_to='videos_uploaded', null=True, verbose_name='Видеофайл')
    video_theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name='main_videos',
                                    blank=True, null=True)
    video_hash = models.CharField(max_length=32, verbose_name="Хэш видео", unique=True, db_index=True, default=None,
                                  editable=False)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.published_at:
            self.published_at = datetime.datetime.now()
        v_hash = self.title + self.description + str(self.published_at)
        self.video_hash = hashlib.md5(v_hash.encode()).hexdigest()
        super().save(*args, **kwargs)


class Theme(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['name']

    def __str__(self):
        return self.name


class VideoTheme(models.Model):
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Основная')
    object = models.Manager()

    class Meta:
        verbose_name = 'Тема видео'
        verbose_name_plural = 'Темы видео'
        unique_together = ('video', 'theme')
        ordering = ['theme__name']

    def __str__(self):
            return f'{self.video} - {self.theme}'

    @classmethod
    def get_sorted_theme(cls, video_hash):
        return cls.objects.filter(video_hash=video_hash).order_by('-is_main', 'theme__name')
