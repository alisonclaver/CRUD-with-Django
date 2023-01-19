from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True, max_length=1000)
    phone = models.CharField(null=True, max_length=500)
    email = models.CharField(null=True, max_length=1500)
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name