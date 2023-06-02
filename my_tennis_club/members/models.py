from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='home/mix/myworldCopy/my_tennis_club/productionfiles/photos/')
    description = models.TextField()

class Member(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	phone = models.IntegerField(null=True)
	joined_date = models.DateField(null=True)
	slug = models.SlugField(default="", null=False)
	def __str__(self):
		return f"{self.firstname} {self.lastname}"
# Create your models here.
