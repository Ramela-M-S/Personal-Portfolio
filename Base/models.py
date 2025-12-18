from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
		name 	= models.CharField(max_length = 30, blank = False)
		email 	= models.EmailField()
		phone_no= models.CharField(max_length = 10, validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits")])
		content = models.TextField(max_length = 300, blank = False)
	
		def  __str__(self):
				return f"{self.name}"
     

     	