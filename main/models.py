from django.db import models


class Card(models.Model):
    question = models.TextField('Вопрос', max_length=256)
    right_answer = models.TextField('Правильный ответ', max_length=100)
    answer1 = models.TextField('Неверный ответ 1', max_length=100)
    answer2 = models.TextField('Неверный ответ 2', max_length=100)
    answer3 = models.TextField('Неверный ответ 3', max_length=100)

    class Meta:
        ordering = ('id',)
        verbose_name = 'карточка вопроса'
        verbose_name_plural = 'Карточки вопросов'

    def __str__(self):
        return f'[{self.id}] {self.question[:20]}...'


class IFile(models.Model):
    value = models.FileField('Файл', upload_to='files/')

    class Meta:
        ordering = ('id',)
        verbose_name = 'файл с вопросами'
        verbose_name_plural = 'Файлы'
