from django.db import models

# Create your models here.

class Todo(models.Model):
	task = models.CharField(max_length=50)
	description = models.TextField()
	deadline = models.CharField(max_length=50)
	completed = models.BooleanField(default=False, blank=True, null=False)

	def __str__(self):
		return self.task