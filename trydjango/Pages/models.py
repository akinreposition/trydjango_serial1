from django.db import models

# Create your models here.
class Page(models.Model):
	title= 		  models.CharField(blank= False, null= True, max_length= 120)
	introduction= models.TextField(blank= False, null= False)
	reviews=      models.CharField(max_length= 200, null=False)
	
	
	
		