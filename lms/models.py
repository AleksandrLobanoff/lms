from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Информация о курсе"""
    tittle = models.CharField(max_length=100, verbose_name='название курса')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

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

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.tittle}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):
    PAYMENT_METHOD = [
        ('cash', 'наличными'),
        ('transfer_to_account', 'перевод на счет')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='даиа оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=19, choices=PAYMENT_METHOD, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.paid_course if self.paid_course else self.paid_lesson} {self.payment_date} {self.payment_amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class CourseSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.user} {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = "Подписки"
