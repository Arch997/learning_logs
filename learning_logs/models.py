from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	"""A topic that the user is learning about."""
	
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		"""Return a string representaion of the model."""
		return self.text
	
class Entry(models.Model):
	"""Something specific about a topic."""
	
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		"""Tell Django to use 'entries' when referring to multiples.

		Without this it would refer to more than one entry as Entrys
		"""
		
		verbose_name_plural = 'entries'
		
	def __str__(self):
		"""Return string representation of the model."""
		if len(self.text) <= 50:
			return self.text[:50]
		else:
			return self.text[:50] + "..."
