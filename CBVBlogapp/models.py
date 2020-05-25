from django.db import models

# Create your models here.

class Blogs(models.Model):
    Title = models.CharField(max_length=500)
    pic = models.FileField(upload_to='images/')
    postedby = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
