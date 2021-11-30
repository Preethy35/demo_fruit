from django.db import models

# Create your models here.

class Fruit1(models.Model):
    fruit_name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.fruit_name