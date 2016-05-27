from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
from django.utils import timezone

# Отделы
class Department(models.Model):
	name = models.CharField(max_length = 4, null = True)
	description = models.TextField(max_length = 140)

	def __str__(self):
		return self.name

# Сотрудники
class Person(models.Model):
    user = models.OneToOneField(User, related_name = "User", null = True)
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.user.username






# Задачи
class Task(models.Model):
	task_name = models.CharField(max_length = 200)
	task_description = models.TextField()
	task_owner = models.ForeignKey(User, related_name = "task_owner", null = True)
	deadline = models.DateTimeField(default=datetime.datetime.now)
	task_performer = models.ForeignKey(User, related_name = "task_performer", null = True)
	status = models.CharField(max_length = 20, default = "Новая")
	wasted_time =  models.IntegerField(default = 0)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.task_name

	def publish(self):
		self.published_date = timezone.now()
		self.save()


# Отчеты
class Results(models.Model):
	task_name = models.ForeignKey(Task)
	task_performer = models.ForeignKey(User)
	wasted_time = models.IntegerField(default = 0)


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
		fields = ['task_name', 'task_description','deadline','task_performer','status','wasted_time']


