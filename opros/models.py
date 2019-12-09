from django.db import models


class Student(models.Model):
	first_name = models.CharField('Имя', max_length=50)
	second_name = models.CharField('Фамилия', max_length=50)
	last_name = models.CharField('Отчество', max_length=50)
	faculty = models.CharField('Факультет', max_length=100)
	course = models.CharField('Курс', max_length=100)
	group = models.IntegerField('Группа')

	def __str__(self):
		return f'{self.second_name} {self.first_name} {self.last_name}; Факультет - {self.faculty}, ' \
			   f'Курс - {self.course}, группа - {self.group}'

	class Meta:
		verbose_name = 'Студент'
		verbose_name_plural = 'Студенты'


class TextAnswer(models.Model):
	answer = models.CharField(name='Ответ', max_length=255)

	def __str__(self):
		return f'Ответ - '

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'


class Question(models.Model):
	answer = models.ForeignKey(TextAnswer, on_delete=models.DO_NOTHING)

	question = models.TextField(name='Вопрос')

	def __str__(self):
		return f'Вопрос - '

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'

