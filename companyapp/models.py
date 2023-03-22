from django.db import models
import datetime

class companydata(models.Model):
	name=models.CharField(max_length=30, null=False, blank=False)
	mail=models.EmailField(max_length=150, blank=True, unique= True)
	phone=models.CharField(max_length=10, null=False, blank=False )
	time=models.TimeField(auto_now=False,auto_now_add=False)
	message=models.TextField(max_length=500, null=False, blank=False)
