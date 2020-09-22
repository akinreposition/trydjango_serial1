from django.db import models

# Create your models here.
class Diary(models.Model):
	Day= models.CharField(max_length=120, blank=False, null=False)
	Topic= models.TextField(blank=False)
	