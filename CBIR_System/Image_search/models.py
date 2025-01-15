from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50 , null=True)
    age = models.IntegerField(default='0000')
    city = models.CharField(max_length=10 , null=True)
    zip = models.PositiveIntegerField(default='0000')
    gender = models.CharField(max_length=50 , null=True)
    image = models.ImageField(upload_to='photos/')
    embedding_id = models.CharField(max_length=50 , null=True)# ID for the embedding in Pinecone
    date = models.DateField(default=datetime.today())

    def __str__(self):
        return self.name
    


