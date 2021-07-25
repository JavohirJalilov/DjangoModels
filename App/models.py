from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	

class Language(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Framework(models.Model):
	name = models.CharField(max_length=30)
	language = models.ForeignKey(Language,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Musician(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	instrument = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name

class Album(models.Model):
	artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	releaase_date = models.DateField(default=timezone.now)
	num_stars = models.IntegerField()

	def __str__(self):
		return self.name