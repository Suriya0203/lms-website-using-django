
from django.db import models
class Image(models.Model):
    name     = models.CharField(max_length=50)
    #roll_num = models.CharField(max_length=100)
    image=models.ImageField(upload_to='topics/%Y/%m/%d/', null=True, blank=True)
    def __str__(self):
        return self.name

# Create your models here.
