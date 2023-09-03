from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Информация о курсе"""
    tittle = models.CharField(max_length=100, verbose_name='название курса')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)

    def __str__(self):
        return f'{self.tittle}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Информация об уроке"""
    tittle = models.CharField(max_length=100, verbose_name='название урока')
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_link = models.TextField(verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.tittle}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
