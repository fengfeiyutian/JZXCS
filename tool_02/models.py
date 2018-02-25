from django.db import models

# Create your models here.
class Blog(models.Model):
	"""docstring for Blog"""
	name = models.CharField(max_length=50, default='dafault name')
	user_id = models.IntegerField(default=1)
	user_name = models.CharField(max_length=20, default='dafault name')
	content = models.CharField(max_length=500, default='dafault content')
	create_at = models.IntegerField(default='1514879938')

	def __str__(self):
		return self.name

class Comment(models.Model):
	"""docstring for Blog"""
	blog_id = models.IntegerField(default=1)
	user_id = models.IntegerField(default=1)
	user_name = models.CharField(max_length=20, default='dafault name')
	content = models.CharField(max_length=500, default='dafault content')
	create_at = models.IntegerField(default='1514879939')

	def __str__(self):
		return self.user_name