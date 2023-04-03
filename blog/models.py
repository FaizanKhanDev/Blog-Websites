from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
 




class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    comment = models.TextField()
    def __str__(self):
        return self.email