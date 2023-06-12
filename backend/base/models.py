# Create your models here.
from django.db import models

# Create your models here.


class item(models.Model):
    todo = models.CharField(max_length = 500, default=None)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField( auto_now_add=True)
    
    
    
    