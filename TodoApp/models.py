from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
	taskname = models.CharField('todo title',max_length=30)
	description = models.TextField()
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return self.title