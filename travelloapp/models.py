from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class Destination(models.Model):

	name = models.CharField(max_length=40)
	image = models.ImageField(upload_to='picture')
	description = models.TextField(max_length=500)
	price = models.IntegerField()
	offer = models.BooleanField(default=False)

	class META:
		verbose_name_plural = "Destination"

	def __str__(self):
		return self.name