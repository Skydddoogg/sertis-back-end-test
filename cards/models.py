from djongo import models

class Card(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length = 100)
    status = models.BooleanField()
    content = models.TextField()
    category = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
