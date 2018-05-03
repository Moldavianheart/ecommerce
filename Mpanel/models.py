from django.db import models

class Account(models.Model):
	username = models.CharField(max_length=60)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=50)
	pin = models.IntegerField(unique=True)
	date  = models.DateTimeField()

class UserSession(models.Model):
	user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
	token = models.CharField(max_length=255)
	user_details = models.CharField(max_length=255)
	date  = models.DateTimeField()

class PasswordReset(models.Model):
	user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
	token = models.CharField(max_length=255)
	date  = models.DateTimeField()
		