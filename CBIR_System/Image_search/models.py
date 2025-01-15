from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default='not_provided')
    city = models.CharField(max_length=10 , default='not_provided')
    zip = models.PositiveIntegerField(default='not_provided')
    gender = models.CharField(max_length=50 , default='not_provided')
    image = models.ImageField(upload_to='photos/')
    embedding_id = models.CharField(max_length=50 , default='not_provided')# ID for the embedding in Pinecone
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name
    


