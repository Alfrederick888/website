from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Вопрос')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    choice_text = models.CharField(max_length=200, verbose_name='Текст ответа')
    votes = models.IntegerField(default=0,verbose_name='Голосов')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выбор'