from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime



# Сотрудники
class Person(models.Model):
    user = models.OneToOneField(User, related_name = "User", null = True)
    department = models.CharField(max_length = 10, default = "zeroDep")

    def __str__(self):
        return self.user.username



# Сообщения
class Messages(models.Model):
	author = models.ForeignKey(Person)
	title = models.CharField(max_length = 20, default = "No Title")
	body = models.TextField(max_length = 200)

	def __str__(self):
		return self.title


# Задачи
class Task(models.Model):
	task_name = models.CharField(max_length = 200)
	task_description = models.TextField()
	task_owner = models.ForeignKey(User, related_name = "task_owner", null = True)
	deadline = models.DateTimeField(default=datetime.datetime.now)
	task_performer = models.ForeignKey(Person, related_name = "task_performer", null = True)
	status = models.CharField(max_length = 20, default = "Новая")
	wasted_time =  models.IntegerField(default = 0)

	def __str__(self):
		return self.task_name


# Формы к каждому из классов

# Сотрудники
class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = ['user', 'department',]



# Задачи
class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['task_name', 'task_description','task_owner','deadline','task_performer','status','wasted_time']

