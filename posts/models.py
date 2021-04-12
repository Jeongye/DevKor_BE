from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    contents = models.TextField()
    date = models.DateTimeField('date made')